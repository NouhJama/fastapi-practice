"""
-This module demonstrates how you can declare path parameters and 
request body at the same time.
-FastAPI will know that the `item_id` is a path parameter and the `item` is a request body,
and will handle them accordingly.
"""

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = 0.0


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    price_with_tax = item.price + item.tax
    return {"item_id": item_id, **item.model_dump(), "price_with_tax": price_with_tax}
