from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
"""
- This example demonstrates how to use the `response_model_include` parameter in FastAPI
    to filter out fields from the response model and ommit the rest of the fields.
- It takes a set of strings to include the response model.
"""
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "price": 30.5, "description": "The bartenders"},
    "baz": {"name": "Baz", "price": 25.1, "description": "The bakers", "tax": 5.0}
}

@app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
async def read_item(item_id: str):
    return items[item_id]