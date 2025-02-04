from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def my_first_fastapi():
    return {
        "Output": "My First FastAPI!!"
    }
