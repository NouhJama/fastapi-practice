from fastapi import FastAPI

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

app = FastAPI()

@app.get("/items/{item_id}/users/{user_id}")
async def read_user_item(item_id: str, user_id: str, q: str | None = None, short: bool = False):
    items = {"item_id": item_id, "user_id": user_id}
    if q:
        items.update({"q": q})
    if not short:
        items.update({"description": "This is a an amazing item that has a long description"})
    return items
