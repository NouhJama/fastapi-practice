from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None

"""
- The same way there is a Query and Path to define extra data for query and path parameters, 
FastAPI provides an equivalent Body.
-For example, extending the previous model, you could decide that you want to have 
another key importance in the same body, besides the item and user.
"""
@app.put("/items/{item_id}")
async def update_item(
    item_id: int, 
    item: Item, 
    user: User, 
    importance: Annotated[int, Body()],
    q: str | None = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results