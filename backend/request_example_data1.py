from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

"""
##Field additional arguments¶
###When using Field() with Pydantic models, you can also declare additional examples:
"""
class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, 
    item: Annotated[Item, Body(embed=True)]
):

    results = {"item_id": item_id, "item": item}
    return results