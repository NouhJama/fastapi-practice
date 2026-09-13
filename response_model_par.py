from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
-This is a pydantic model that defines the structure of the request and response data for the /items/ endpoint.
-The Item model has four fields: name, description, price, and tax. The name and price fields are required, 
while the description and tax fields are optional.
-You can use this model to validate incoming request data and to generate the response data for the endpoint.
-Return as an instance of the Item model, which will be automatically serialized to JSON and returned to the client.
-You can also use return a list of Item instances, which will be serialized to a JSON array and returned to the client.
"""
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item

# Return a list of Item instances
@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        Item(name="Item 1", description="Description 1", price=10.0, tax=1.0),
        Item(name="Item 2", description="Description 2", price=20.0, tax=2.0),
    ]
