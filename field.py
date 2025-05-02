from pydantic import BaseModel,Field
from typing import List, Dict, Optional

class Cart(BaseModel):
    userID:int
    items:List[str]
    qty:Dict[str,int]

class BlogPost(BaseModel):
    title:str
    content:str
    img:Optional[str]=None

class Employee(BaseModel):
    id:int
    name:str=Field(
        ...,
        min_length=3,
        max_length=50,
        description='Employee name required',
        example='Manus'
        )
    dept:Optional[str]='General'
    salary:float=Field(...,ge=10000)