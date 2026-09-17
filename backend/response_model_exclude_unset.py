from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "price": 30.5, "description": "The bartenders"},
    "baz": {"name": "Baz", "price": 25.1, "description": "The bakers", "tax": 5.0},
    "qux": {"name": "Qux", "price": 10.5, "tax": 1.0, "tags": ["rock", "metal"]},
}

"""
- This example demonstrates how to use the `response_model_exclude_unset` parameter in FastAPI
 to filter out unset fields from the response model.
- This only includes the values that were explicitly set in the response, excluding any default values or unset fields.
"""

@app.post("/items/", response_model=Item, response_model_exclude_unset=True)
async def create_item(item_id: str):
    return items[item_id]

@app.get("/items/", response_model=list[Item], response_model_exclude_unset=True)
async def read_items():
    return list(items.values())
