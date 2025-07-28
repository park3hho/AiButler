import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

TORTOISE_ORM = {
    "connections": {
        "default": os.getenv("DATABASE_URL")  # .env의 값 사용
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],  # aerich.models는 필수
            "default_connection": "default",
        },
    },
}
