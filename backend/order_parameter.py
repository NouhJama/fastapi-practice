from fastapi import FastAPI, Path

app = FastAPI()

""""
- This file demonstrated how to order path parameters in FastAPI.
- In FastAPI, the order of path parameters in the function definition does not affect how they
are matched in the URL path. FastAPI will correctly match the parameters based on their names and types, regardless of their order in the function definition.
- In this example, we have a path parameter 'item_id' and a query parameter 'q'. The order of these parameters in the function definition does not affect how they are matched in the URL path.
- The path parameter 'item_id' is defined using the 'Path' function.
"""
@app.get("/items/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results