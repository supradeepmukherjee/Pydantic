from pydantic import BaseModel,field_validator,model_validator,computed_field
from typing import List, Dict, Optional

class User(BaseModel):
    name:str
    @field_validator('name')
    def nameLen(cls,v):
        if len(v)<4:
            raise ValueError('Name must be atleast 4 characters')
        return v

class SignupData(BaseModel):
    password:str
    confirmPassword:str
    @model_validator(mode='after')
    def matchPassword(cls,v):
        if values.password!=values.confirmPassword:
            raise ValueError('Passwords don\'t match')
        return v

class Product(BaseModel):
    price:float
    qty:int
    @computed_field
    @property
    def totalPrice(self)->float:
        return self.price*self.qty