from typing import Optional, List
from pydantic import BaseModel
from pydantic.tools import T

"""
We Two Types Of Model in FastAPI
1. Pydantic Model - We call it Schema
2. SqlAlchemy Model
"""
class BlogBase(BaseModel):
    title:str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True



    
class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUserInBlog(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]= []

    class Config():
        orm_mode = True





class ShowBlog(Blog):
    title:str
    body: str
    creator: ShowUserInBlog
    
    class Config():
        orm_mode = True



class Login(BaseModel):
    username:str
    password:str

    class Config():
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None