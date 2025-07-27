# 최신의 ubuntu 이미지를 기반으로 설정
FROM python:3.12-slim
# 사용자
LABEL authors="iwill"

# 작업 디렉토리 설정
WORKDIR /app

RUN pip cache purge
# uv 설치 (Rust 기반이지만 바이너리 제공됨)
RUN pip install uv

# 리눅스 환경 이미지 파일 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 의존성 정보 복사
COPY requirements.txt .
COPY uv.lock .

# 의존성 설치
RUN pip install --upgrade pip setuptools wheel
RUN uv pip install -r requirements.txt --system

# 소스 코드 복사
COPY . .


# FastAPI 앱 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

