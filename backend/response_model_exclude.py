from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
- response_model_exclude: Exclude specific fields from the response model.
- Include the rest of the fields in the response model.
- This also demonstrates that you can use list instead of set for the exclude parameter.
- Pydantic still converts the list to a set internally, so you can use either.
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

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def read_public_item(item_id: str):
    return items[item_id]