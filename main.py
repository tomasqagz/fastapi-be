from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()

class Player(BaseModel):
    id: int
    name: str
    level: int
    race : str
    p_class: str
    created_at: datetime = datetime.now()

@app.get("/")
def read_root():
    return {"Bye": "World"}


