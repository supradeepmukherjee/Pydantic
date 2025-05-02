from fastapi import FastAPI,Depends
from pydantic import BaseModel,EmailStr

app=FastAPI()

class User(BaseModel):
    name:str
    email:EmailStr
    password:str

class Settings(BaseModel):
    appName:str='New App'
    admin_email:str='admin@app.in'

def getSettings():
    return Settings

@app.post('/sign-up')
def signUp(user:User):
    return {'msg':f'{user.name} Signed Up Successfully'}

@app.get('/settings')
def getSettingsEndpoint(settings:Settings=Depends(getSettings)):#learn
    return {}