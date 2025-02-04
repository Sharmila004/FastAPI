from fastapi import FastAPI
from pydantic import BaseModel

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

class User(BaseModel): # since to us ethis class as a pydantic base model, it has to inherit from pydantic's base model
    username : str
    date_joined : str
    location : str
    age : int

app  = FastAPI()

@app.get('/users')
def get_user_query(limit: int = 20):
    user_list = list(user_database.values())
    return user_list[ : limit]

# post operation
@app.post('/')
def create_user(user: User):
    username = user.username
    user_database[username] = user.dict()
    return {'message' : f"Successfully created user: {username}" }