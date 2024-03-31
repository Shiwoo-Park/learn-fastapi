import os
import platform
from fastapi import APIRouter

from enums import ModelName

router = APIRouter()


@router.get("/models/{model_name}")
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


@router.get("/server-info")
async def get_server_info():
    server_info = {
        "hostname": platform.node(),
        "system": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "memory_total_mb": os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024.0 ** 2),
        # 기타 필요한 서버 환경 정보를 추가할 수 있습니다.
    }
    return server_info