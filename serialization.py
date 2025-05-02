from pydantic import BaseModel,field_validator,model_validator,computed_field,ConfigDict
from typing import List, Dict, Optional
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    code:str

class User(BaseModel):
    id:int
    name:str
    email:str
    isActive:bool=True
    createdAt:datetime
    address:Address
    tags:List[str]=[]
    model_config=ConfigDict(json_encoders={datetime:lambda v:v.strftime('%d-%m-%Y %H:%M:%S')})#learn this

user=User(
    id=1,
    name='manus',
    email='test@mail.com',
    createdAt=datetime(2025,1,15,15,44),
    address=Address(
        street='elaka',
        city='Hindupur(Erstwhile Islamabad)',
        code='000000'
    ),
    tags=['premium','subscriber']
)

# Using model_dump()->dict
user_dict=user.model_dump()

# Using model_dump_json()->dict
user_json=user.model_dump_json()
print(user_json)