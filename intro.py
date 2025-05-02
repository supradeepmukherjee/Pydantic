from pydantic import BaseModel

class User(BaseModel):
    id: int
    name:str
    isActive:bool

data={
    'id':1,
    'name':'test',
    'isActive':True
}

user=User(**data)
print(user)