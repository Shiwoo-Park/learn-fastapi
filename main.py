import logging

from fastapi import FastAPI

# setup loggers
from apis import item, sample

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


app.include_router(item.router)
app.include_router(sample.router)
