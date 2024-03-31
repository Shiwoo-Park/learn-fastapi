import os
import requests
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


# ecs fargate 에서 
@router.get("/fargate-info")
async def get_instance_info():
    METADATA_URL = "http://169.254.170.2/v2/metadata"
    try:
        response = requests.get(METADATA_URL, timeout=0.1)
        if response.status_code == 200:
            metadata = response.json()
            instance_info = {
                "instance_id": metadata["TaskARN"].split("/")[-1],
                "instance_type": metadata["Resource"]["ARN"],
                "availability_zone": metadata["AvailabilityZone"],
                "region": metadata["Region"],
                "os_platform": os.getenv("OS", "Unknown"),
                "python_version": os.getenv("PYTHON_VERSION", "Unknown"),
                "cpu_count": os.cpu_count(),
                "memory_total_mb": os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024.0 ** 2),
                # 추가할 환경 변수 정보들을 여기에 추가합니다.
            }
            return instance_info
    except Exception as e:
        pass
    return {"error": "Failed to retrieve instance information"}


@router.get("/ec2-info")
async def get_instance_info():
    instance_info = {
        "instance_id": os.getenv("INSTANCE_ID", "Unknown"),
        "instance_type": os.getenv("INSTANCE_TYPE", "Unknown"),
        "availability_zone": os.getenv("AVAILABILITY_ZONE", "Unknown"),
        "region": os.getenv("REGION", "Unknown"),
    }
    return instance_info



@router.get("/ec2-info-v2")
async def get_ec2_instance_info():
    METADATA_URL = "http://169.254.169.254/latest/meta-data"

    try:
        response = requests.get(METADATA_URL, timeout=0.1)
        if response.status_code == 200:
            metadata = response.text
            instance_id = requests.get(f"{METADATA_URL}/instance-id").text
            instance_type = requests.get(f"{METADATA_URL}/instance-type").text
            availability_zone = requests.get(f"{METADATA_URL}/placement/availability-zone").text
            region = availability_zone[:-1]
            os_platform = os.getenv("OS", "Unknown")
            python_version = os.getenv("PYTHON_VERSION", "Unknown")
            cpu_count = os.cpu_count()
            memory_total_mb = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024.0 ** 2)
            # 추가할 환경 변수 정보들을 여기에 추가합니다.
            instance_info = {
                "instance_id": instance_id,
                "instance_type": instance_type,
                "availability_zone": availability_zone,
                "region": region,
                "os_platform": os_platform,
                "python_version": python_version,
                "cpu_count": cpu_count,
                "memory_total_mb": memory_total_mb,
                # 추가할 EC2 인스턴스 정보들을 여기에 추가합니다.
            }
            return instance_info
    except Exception as e:
        pass
    return {"error": "Failed to retrieve EC2 instance information"}
