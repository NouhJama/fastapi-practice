from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

"""
- This file demonstrates how to validate path parameters in FastAPI.
- Using the 'Path' function from FastAPI, we can add validation rules to path parameters
- In this example, we validate that 'item_id' is an integer and provide a title for the parameter.
- We also add a validation rule that 'item_id' must be greater than or equal to 1 using 
the 'ge' parameter in the 'Path' function, also you can use 'gt' for greater than, 
'le' for less than or equal to, and 'lt' for less than.
- It can also be added a metadata to the path parameter, such as a title, description, and example, 
which can be used in the generated OpenAPI documentation.
"""

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(
        title="The ID of the item to get",
        gt=0, # item_id must be greater than 0
        le=1000)], # item_id must be less than or equal to 1000
        q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results