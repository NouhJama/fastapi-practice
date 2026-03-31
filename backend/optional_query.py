"""
This demonstrates how to use optional query parameters in FastAPI. 
The `skip` and `limit` parameters allow clients to control pagination
when retrieving items from the `fake_items_db`. 
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}