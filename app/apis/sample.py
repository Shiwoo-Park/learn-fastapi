import os
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


@router.get("/instances")
async def get_instance_info():
    instance_info = {
        "instance_id": os.getenv("INSTANCE_ID", "Unknown"),
        "instance_type": os.getenv("INSTANCE_TYPE", "Unknown"),
        "availability_zone": os.getenv("AVAILABILITY_ZONE", "Unknown"),
        "region": os.getenv("REGION", "Unknown"),
    }
    return instance_info