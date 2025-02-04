from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

user_database = {
    'jack': {
        "username" : "jack",
        "date_joined" : "2021-12-01",
        "location" : "New York",
        "age" : 28
    },
    'jill': {
        "username" :"jill",
        "date_joined" : "2021-12-02",
        "location" : "Los Angeles",
        "age" : 19
    },
    'jane': {
        "username" : 'jane',
        "date_joined" : "2021-12-03",
        "location" : "Toronto",
        "age" : 52
    }
}

class User(BaseModel):
    username : str = Field(min_length= 3, max_length= 20)
    date_joined : date
    location : Optional[str] = None
    age : int = Field(None, gt=5, lt=130)

app = FastAPI()

# get operations
@app.get('/users')
def get_user_query(limit : int = 20):
    user_list = list(user_database.values())
    return user_list[:limit]

@app.post('/')
def create_user(user: User):
    username = user.username
    user_database[username] = user.dict()