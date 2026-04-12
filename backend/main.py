from fastapi import FastAPI

app = FastAPI()



@app.get("/items/{item_id}")
def read_items(item_id: int):
    return {"item_id": item_id}


