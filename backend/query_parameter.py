from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    Retrieve a list of items with optional pagination.
    This uses the list slicing syntax to return a subset of items from the fake_items_db based on the skip and limit query parameters.

    - **skip**: Number of items to skip (default is 0)
    - **limit**: Maximum number of items to return (default is 10)
    - **Returns**: A list of items from the fake_items_db based on the skip and limit parameters.
    """
    return fake_items_db[skip : skip + limit]

