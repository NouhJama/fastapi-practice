from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
"""
-This example shows how to add examples to the schema of a model, 
which will be used in the OpenAPI documentation.
- The example is added to the "json_schema_extra" configuration of the model,
which allows you to provide additional information for the JSON schema generation.
- When using Field() with Pydantic models, you can also declare additional examples.
"""

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: float | None = Field(default=None, example=3.2)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results