import os
from urllib.parse import urljoin
import requests
from .channel import Channel

class Device:
    def __init__(self,name,api_url=None,api_key=None,verify=True,check=True):
        self.api_url = os.environ.get('IOT_API_URL',api_url)
        if self.api_url is None:
            raise Exception("Must provide api_url argument or set IOT_API_URL environment variable")
        self.api_key = os.environ.get('IOT_API_KEY',api_key)
        if self.api_key is None:
            raise Exception("Must provide api_key argument or set IOT_API_KEY environment variable")
        self.headers = {"api_key":self.api_key}
        self.name = name
        self.verify=verify
        if check:
            url = urljoin(self.api_url,f'db/Device?name={self.name}')
            r = requests.get(url,verify=self.verify,headers=self.headers)
            if r.status_code != 200:
                raise Exception(f"Could not communicate with api. {r.text}")
            data = r.json()
            if len(data)!=1:
                raise Exception(f"No device named {self.name} found in database")
        
    @property
    def channels(self):
        url = urljoin(self.api_url,f"db/DataChannel?device={self.name}")
        r = requests.get(url,verify=self.verify,headers=self.headers)
        if r.status_code!=200:
            raise Exception(f"Could not fetch channels. {r.text}")
        return [Channel(i['id'],api_url=self.api_url,api_key=self.api_key,verify=self.verify) for i in r.json()]
    

