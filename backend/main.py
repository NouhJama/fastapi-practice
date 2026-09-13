from fastapi import FastAPI, HTTPException

app = FastAPI()

# fake empty dict to simulate database
fake_items_db : dict = {}

# Create an item pydantic model with only name and price fields 
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

# Create an endpoint to create an item with item_id as path parameter and item as body parameter
@app.post("/items/{item_id}", status_code=201)
def create_item(item_id: int, item: Item):
    # Check if item_id already exists in fake_items_db, if it does, raise HTTPException with status code 400 and detail "Item already exists"
    if item_id in fake_items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_items_db[item_id] = item
    return item

@app.get("/")
def health_check():
    return {"status": "ok"}



@app.get("/items/{item_id}")
def read_items(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]

