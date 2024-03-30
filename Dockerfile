# 기반 이미지 설정
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY ./app /app

# 의존성 설치
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 포트 설정 (FastAPI 기본 포트)
EXPOSE 80

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
