from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Model(str, Enum):
    name = "xiaowu"
    age = "18"
    address = "beijing"


@app.get("/{id}")
async def func(id: int) -> dict:
    return {"id": id}


@app.get("/model/{model_type}")
async def get_model(model_type: Model):
    if model_type is Model.name:
        return {"model_name": model_type, "message": "111"}
    elif model_type == Model.age:
        return {"model_age": model_type, "message": "222"}
    else:
        return 666


from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    return item
