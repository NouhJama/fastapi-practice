from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

"""
- This example demonstrates how to use a base model to filter out sensitive data from the response.
- The `BaseUser` model contains only the fields that should be returned in the response, 
while the `UserIn` model includes all fields, including sensitive ones like `password`.
- This approach takes advantage of class inheritance to create a clear separation between input and output data models,
 ensuring that sensitive information is not exposed in the API response.
- With this, we get tooling support, from editors and mypy as this code is correct in terms of types, 
but we also get the data filtering from FastAPI. 
-Now, for FastAPI, it will see the return type and make sure that what you return includes only the fields
 that are declared in the type
"""

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.post("/users/")
async def create_user(user: UserIn) -> BaseUser:
    return user