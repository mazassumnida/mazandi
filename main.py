from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/{handle}")
def read_item(handle: str):
    return {"handle": handle}
