"""
This module demonstrates how to use required query parameters in FastAPI.
In this example, both `skip` is required and must be provided by the client, while `limit` has a default value of 10.
You can also use multiple query paramters and define some as required and some as optional. 
In this example, `needy` is a required query parameter that must be 
provided by the client when making a request to the `/items/{item_id}` endpoint.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, 
                         needy: str, 
                         skip: int = 0, 
                         limit: int | None = 10
                         ):
    items = {"item_id": item_id, "needy": needy}
    return items
        