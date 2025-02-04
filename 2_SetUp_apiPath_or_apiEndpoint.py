from fastapi import FastAPI

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

app = FastAPI()

# all users
@app.get('/users')
def get_users():
    user_list = list(user_database.values())
    return user_list

#specific users with Path Parameter
@app.get('/users/{username}')
def get_users_path(username : str):
    return user_database[username]

#specific users with Query Parameter
@app.get('/users')
def get_users_query(limit : int):
    user_list  = list(user_database.values())
    return user_list[:limit]