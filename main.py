from flask import Flask
from messages import messages
from random import choice

app = Flask(__name__)


@app.get("/")
def root():
    message = choice(messages)
    return {"message": message}
