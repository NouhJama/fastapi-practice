"""
-This file demonstates how to validate path parameters in FastAPI.
-Using the 'Path' function from FastAPI, we can add validation rules to path parameters.
-In this example, we validate that 'item_id' is an integer and provide a title for the parameter.
- It can also be added a metadata to the path parameter, such as a title, description, and example, 
which can be used in the generated OpenAPI documentation.
"""

from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results