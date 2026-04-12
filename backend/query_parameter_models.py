from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()
"""
This file demonstrates how to use Pydantic models to define and validate query parameters in FastAPI.
- We define a Pydantic model 'FilterParams' that includes several fields with validation rules and metadata.
- The 'model_config' with 'extra': 'forbid' is used to prevent any extra fields from being included in the query parameters.
- FastAPI will extract the data for each field from the query parameters in the request and give you the Pydantic model you defined.
"""

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query