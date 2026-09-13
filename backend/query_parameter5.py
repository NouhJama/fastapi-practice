"""
- This module demonstrates how to validate the query parameters using
annotations and the `Query` class from FastAPI. 
- The `Query` class allows you to specify additional validation rules 
 for query parameters, such as minimum and maximum values, regular expressions, and more.
   """

from fastapi import FastAPI, Query
from typing import Annotated
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results