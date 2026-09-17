from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

def fake_hash_password(password: str):
    return "supersecret" + password

def fake_save_user(user_in: "UserIn"):
    hashed_password = fake_hash_password(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

class UserIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserInDB(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str
    full_name: str | None = None