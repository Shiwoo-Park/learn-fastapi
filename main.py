import logging
from datetime import datetime
from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from enums import ModelName

# setup loggers
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)
# the __name__ resolve to "main" since we are at the root of the project.
# This will get the root logger since no logger in the configuration has this name.

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
async def create_item(item: Item):
    data = item.dict()
    data["response_time"] = datetime.now()
    return data


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    """
    :param item_id: 아이템 ID, path param<br/>
    :param item: 업데이트 할 아이템 정보<br/>
    :param q: 쿼리 파라미터 예시. 디폴트값이 None 이기에 required 아닌것으로 인식<br/>
    :return: 업데이트 후 아이템 정보
    """
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
