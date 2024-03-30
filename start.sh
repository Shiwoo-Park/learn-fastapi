# application root path 로 이동
cd app
#  main.py 파일의 FastAPI() 객체 변수명인 app 활용
uvicorn main:app --reload