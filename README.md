# learn-fastapi

## 개요

- python 3.9.x
- fastapi

## 기본 기능

- 데이터 검증: 타입, enum 등
  - [pydantic](https://pydantic-docs.helpmanual.io/)
- 자동 문서화 (API Spec)
  - [Swagger style](http://127.0.0.1:8000/docs) : `/docs`
  - [ReDoc style](http://127.0.0.1:8000/redoc) : `/redoc`
  - [Open API JSON](http://127.0.0.1:8000/openapi.json) : `/openapi.json`

## 명령어

```shell
# installation
./install.sh

# 서버시작
./start.sh
```