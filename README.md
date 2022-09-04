# learn-fastapi

## 기본 기능
- 데이터 파싱
- 데이터 검증: 타입, enum 등
- 자동 문서화 (API Spec)
  - [Swagger style](http://127.0.0.1:8000/docs) : `/docs`
  - [ReDoc style](http://127.0.0.1:8000/redoc) : `/redoc`
  - [Open API JSON](http://127.0.0.1:8000/openapi.json) : `/openapi.json`

## 튜토리얼
- 참고자료
  - [Repo: fastapi-boilerplate](https://github.com/teamhide/fastapi-boilerplate)


## 명령어

```shell
# FastAPI 풀패키지 설치
pip install "fastapi[all]"

# 서버시작 (main.py 파일의 FastAPI() 객체 변수명인 app 활용)
uvicorn main:app --reload
```