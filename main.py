from fastapi import FastAPI
from messages import messages
from random import choice

app = FastAPI()


@app.get("/")
def root():
    message = choice(messages)
    return {"message": message}
