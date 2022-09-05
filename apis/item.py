from datetime import datetime
from typing import Optional, Union

from fastapi import APIRouter

from models import Item

router = APIRouter()


@router.get("/items")
async def get_item_list(page: int = 1, count: int = 20):
    """
    아이템 리스트 반환
    :param page: 페이지번호<br/>
    :param count: 불러올 개수<br/>
    :return: 아이템 리스트
    """
    return {"items": ["aaa", "bbb", "ccc"], "page": page, "count": count}


@router.get("/items/{item_id}")
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


@router.post("/items")
async def create_item(item: Item):
    data = item.dict()
    data["response_time"] = datetime.now()
    return data


@router.put("/items/{item_id}")
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
