import os
from contextlib import asynccontextmanager # asynccontextmanager 임포트
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from tortoise import Tortoise # register_tortoise 임포트
from dotenv import load_dotenv

# 라우터 임포트
from app.stimuli.routers.v1.main_page import router as channel_router
from app.stimuli.routers.v1.loginout_router import router as token_router
from app.stimuli.routers.v1.register_router import router as user_router
from app.brain.routers.v1.accept_textual_stimuli import router as accept_textual_stimuli_router

from app.configs.postgres import TORTOISE_ORM

load_dotenv()


# lifespan 컨텍스트 매니저 정의
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup complete.")

    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

    yield # 애플리케이션이 실행되는 동안 대기

    print("Application shutdown complete.")


# FastAPI 애플리케이션 인스턴스 생성
# lifespan 인자를 사용하여 정의된 lifespan 컨텍스트 매니저를 연결합니다.
app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan # lifespan 컨텍스트 매니저 연결
)

app.include_router(channel_router)
app.include_router(accept_textual_stimuli_router)
app.include_router(user_router)
app.include_router(token_router)

