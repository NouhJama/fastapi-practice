"""
This modules demonstrates how to use multiple query parameters in FastAPI, 
including type conversion.
The `skip` and `limit` parameters allow clients to control pagination when retrieving items from the
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
        {"description": "This is an amazing item that has a long description"}
    )
    return item