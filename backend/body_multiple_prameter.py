from typing import Annotated

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()
"""
 - This file demonstrates how to mix multiple path parameters and query parameters in a single endpoint in FastAPI.
 - In this example, we have a path parameter 'item_id' and a query parameter 'q'. We also have a request body parameter 'item' which is an instance of the Pydantic model 'Item'.
 - The path parameter 'item_id' is defined using the 'Path' function, while the query parameter 'q' is defined as a regular function parameter with a default value of None.
 - The request body parameter 'item' is defined as an instance of the Pydantic model 'Item', which includes several fields with validation rules and metadata.
 - FastAPI will extract the data for each parameter from the appropriate part of the request (path, query, or body)
"""

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
    user: User | None = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results