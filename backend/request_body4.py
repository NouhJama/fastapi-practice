from fastapi import FastAPI
from pydantic import BaseModel
"""
- This module demonstrates how you can declare path parameters, 
query parameters, and request body at the same time.
- FastAPI will know that the `item_id` is a path parameter, 
the `q` is a query parameter, and the `item` is a request body,
and will handle them accordingly.
"""
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if item.tax:
        price_with_tax = item.price + item.tax
        result.update({"price_with_tax": price_with_tax})
    if q:
        result.update({"q": q})
    return result