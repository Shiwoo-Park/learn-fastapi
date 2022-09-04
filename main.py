from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from enums import ModelName

app = FastAPI()


@app.get("/")
async def root():
    """
    Root path
    - API 응답 가능 타입: dict, list, str, int, Pydantic model
    """
    return {"message": "Hello world"}
    # return ["aaa", "bbb"]
    # return "Hello world"


@app.get("/items")
async def get_item_list(page: int = 1, count: int = 20):
    """
    아이템 리스트 반환
    :param page: 페이지번호<br/>
    :param count: 불러올 개수<br/>
    :return: 아이템 리스트
    """
    return {"items": ["aaa", "bbb", "ccc"], "page": page, "count": count}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
    """
    :param item_id: 숫자만 입력 가능<br/>
    :param q: optional<br/>
    :param short: y|yes|on|True|true|1 일때 True 로 인식<br/>
    :return: 특정 item 불러오기
    """
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if short:
        item.update({"description": "This is short item"})
    return item


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    모델 정보를 얻는다

    :param model_name: 모델 종류 (choice 필드)<br/>
    :return 모델정보
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post("/items")
async def create_item(item: Item) -> Item:
    return item
