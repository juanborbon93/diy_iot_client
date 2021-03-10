import requests
from pydantic import BaseModel,validate_arguments
from typing import List

class ChannelConfig(BaseModel):
    name:str
    data_type:str
class DeviceConfig(BaseModel):
    name:str
    channels:List[ChannelConfig]

@validate_arguments
def register_device(device_config:DeviceConfig,api_url=None,api_key=None,verify=True,check=True):
    api_url = os.environ.get('IOT_API_URL',api_url)
    if api_url is None:
        raise Exception("Must provide api_url argument or set IOT_API_URL environment variable")
    api_key = os.environ.get('IOT_API_KEY',api_key)
    if api_key is None:
        raise Exception("Must provide api_key argument or set IOT_API_KEY environment variable")
    headers = {"api_key":api_key}
    url = urljoin(api_url,'api/register_device')
    r = requests.post(url,json=device_config.dict(),headers=headers,verify=verify)
    if r.status_code != 200:
        raise Exception(f"Failed to register device. {r.text}")