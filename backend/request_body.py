from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

"""
This module demonstrates how to use request bodies in FastAPI.
The `Item` class is defined as a Pydantic model, which allows FastAPI 
to automatically validate and serialize the request body data.
"""
@app.post("/items/")
async def create_item(item: Item):
    return item

