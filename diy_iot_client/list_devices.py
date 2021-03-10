import requests 
from urllib.parse import urljoin
from .device import Device
import os
def list_devices(api_url=None,api_key=None,verify=True):
    api_url = os.environ.get('IOT_API_URL',api_url)
    if api_url is None:
        raise Exception("Must provide api_url argument or set IOT_API_URL environment variable")
    api_key = os.environ.get('IOT_API_KEY',api_key)
    if api_key is None:
        raise Exception("Must provide api_key argument or set IOT_API_KEY environment variable")
    headers = {"api_key":api_key}
    url = urljoin(api_url,"db/Device")
    r = requests.get(url,headers=headers)
    if r.status_code != 200:
        raise Exception(f"Could not fetch list of devices. {r.text}")
    return [Device(i.get("name"),api_url=api_url,api_key=api_key,verify=verify) for i in r.json()]