from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import RedirectResponse  # 필요 시 사용 (현재는 JSON 응답)

# 인증 관련 함수 임포트 (비밀번호 검증)
from app.stimuli.functions.auth import AuthFunction

# Pydantic DTOs 임포트 (응답 데이터 모델)
from app.stimuli.dtos.token_dto import Token  # 토큰 관련 DTO 임포트

# JWT 토큰 생성 및 검증 관련 함수 임포트
from app.stimuli.functions.tokening import (
    create_access_token,
)

# 데이터베이스 모델 임포트
from app.models.users import UserModel

# Tortoise ORM 예외 임포트
from tortoise.exceptions import DoesNotExist

router = APIRouter(prefix="", tags=["Authentication"])


@router.post("/login", response_model=Token)
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    try:
        user = await UserModel.get(email=email)
        if not AuthFunction.verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # 로그인 성공 시 JWT 액세스 토큰과 리프레시 토큰 생성
        access_token = create_access_token(data={"sub": str(user.id)})

        # ✅ 쿠키에 JWT 저장 + 리디렉션
        response = RedirectResponse(url="/dashboard", status_code=303)
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,  # JS에서 접근 불가 — 보안 강화
            secure=False,  # HTTPS에서만 쓸 경우 True
            samesite="lax",  # CSRF 방지 (필요 시 strict)
        )
        return response

    except DoesNotExist:
        raise HTTPException(status_code=401, detail="Incorrect email or password")


@router.post("/logout")
async def logout():
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie(
        key="access_token", httponly=True, secure=False, samesite="lax"
    )
    return response


