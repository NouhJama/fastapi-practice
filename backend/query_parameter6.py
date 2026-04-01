"""
This demonstrates how to make the query parameter accept a list of strings.
The `Query` class is used to specify that the query parameter `q` can be a
list of strings. 
- You can also define a default value for the list if None is provided.
- You can also add additional metadata to the query parameter using the `Query` class.
"""

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[list[str] | None, 
    Query(
        title="Query string",
        description="A list of query strings to search for in the items.",
        max_length=50,
        min_length=3,
        example=["foo", "bar"]
        )] = ["foo", "bar"]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results