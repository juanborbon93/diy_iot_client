from pydantic import BaseModel
from datetime import datetime
from typing import Union,Dict

class ChannelEntry(BaseModel):
    time:datetime
    numeric_value:Union[int,float]
    metadata:Dict
