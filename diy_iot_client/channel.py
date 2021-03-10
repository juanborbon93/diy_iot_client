from datetime import datetime
from urllib.parse import urljoin
from .channel_entry import ChannelEntry
from pydantic import BaseModel,validate_arguments,Field
from typing import Dict,List,Union
import os
import requests

class ChannelDataLog(BaseModel):
    numeric_value:float
    metadata:Dict=None
    time:datetime = Field(default_factory=datetime.utcnow)

class Channel:
    def __init__(self,id,api_url=None,api_key=None,verify=True,check=True):
        self.api_url = os.environ.get('IOT_API_URL',api_url)
        if self.api_url is None:
            raise Exception("Must provide api_url argument or set IOT_API_URL environment variable")
        self.api_key = os.environ.get('IOT_API_KEY',api_key)
        if self.api_key is None:
            raise Exception("Must provide api_key argument or set IOT_API_KEY environment variable")
        self.headers = {"api_key":self.api_key}
        self.id = id
        self.verify=verify
        url = urljoin(self.api_url,f'db/DataChannel?id={self.id}')
        r = requests.get(url,verify=self.verify,headers=self.headers)
        if r.status_code != 200:
            raise Exception(f"Could not communicate with api. {r.text}")
        data = r.json()
        if len(data)!=1:
            raise Exception(f"No device named {self.name} found in database")
        data = data[0]
        self.name = data.get("name")
        self.device = data.get("device")
        self.data_type = data.get("data_type")
        self.data_log = []
    def get_data(start_time:datetime=None,end_time:datetime=None):
        endpoint = f"api/query_device_data/{self.device}?channel={self.id}"
        if start_time:
            endpoint += f"&start_time={start_time}"
        if end_time:
            endpoint += f"&end_time={end_time}"
        url = urljoin(self.api_url,endpoint)
        r = requests.get(url,verify=self.verify,headers=self.headers)
        if r.status_code!=200:
            raise Exception(f"Error getting chnanel data. {r.text}")
        return [ChannelEntry(**k) for k in r.json()]
    @validate_arguments
    def log_data(self,data:Union[ChannelDataLog,List[ChannelDataLog]]):
        if not isinstance(data,list):
            data = [data]
        for entry in data:
            self.data_log.append({
                "channel":self.name,
                "numeric_value":entry.numeric_value,
                "metadata":entry.metadata,
                "time":str(entry.time)
            })
        
        
