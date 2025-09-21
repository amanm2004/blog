from typing import List

from pydantic import BaseModel


class Blogbase(BaseModel):
    title: str
    body: str

   

class Blog(Blogbase):
    class Config():
     from_attributes= True
   


class User(BaseModel):
    name: str
    email: str
    password: str


class showUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]=[]

    class Config():
     from_attributes= True


class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser

    class Config():
       from_attributes= True
  