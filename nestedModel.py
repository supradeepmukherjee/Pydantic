from pydantic import BaseModel,field_validator,model_validator,computed_field
from typing import List, Dict, Optional

class Address(BaseModel):
    street:str
    city:str
    postalCode:str

class User(BaseModel):
    id:int
    name:str
    address:Address

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None

Comment.model_rebuild()

address=Address(
    street='Pakistan MC',
    city='Hindupur(Erstwhile Islamabad)',
    postalCode:'000000'
)

user=User(
    id=1,
    name='manus',
    address=address
)

comment=Comment(
    id=1,
    content:'1st',
    replies=[
        Comment(
            id=2,
            content:'reply1'
        ),
        Comment(
            id=3,
            content:'reply2'
        ),
    ]
)