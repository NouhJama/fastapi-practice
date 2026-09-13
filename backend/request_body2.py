"""
-Use the models
-Inside the function, you can access all the attributes of the model object directly.

"""
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    # Convert the Pydantic model to a dictionary
    item_dict = item.model_dump()
    if item.tax:
        # Calculate the price with tax and add it to the dictionary
        price_with_tax = item.price + item.tax
        # Update the dictionary with the new key-value pair
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

