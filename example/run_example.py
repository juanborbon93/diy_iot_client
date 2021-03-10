from device import Feed
from diy_iot_client import Device,list_devices
import os
from time import sleep

api_url = os.environ.get('IOT_API_URL',"http://localhost:5000/")
devices = list_devices(api_url=api_url,api_key="dev",verify=False)

feeds_dict = {}
for device in devices:
    feeds_dict[device.name] = {channel.name:Feed() for channel in device.channels}


while True:
    for device in devices:
        for channel in device.channels:
            channel.log_data({"numeric_value":feeds_dict[device.name][channel.name].get_value()})
        sleep(1)
        device.push_data()
