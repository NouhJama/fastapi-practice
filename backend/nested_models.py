from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

"""
Each attribute of a Pydantic model has a type.
But that type can itself be another Pydantic model.
So, you can declare deeply nested JSON "objects" with specific attribute names, types and validations.
All that, arbitrarily nested.
Define a submodel¶
For example, we can define an Image model:
- and then use it as a type of an attribute of another model, such as Item.
"""
class Image(BaseModel):
    # The HttpUrl type is a special type provided by Pydantic.
    # You need to import it from pydantic to use it.
    url: HttpUrl | None = None
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    # The type of the images attribute is a list of submodels of type Image.
    images: list[Image] | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results