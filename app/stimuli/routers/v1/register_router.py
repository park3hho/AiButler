from fastapi import APIRouter, Request, Form, HTTPException, status, Depends
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

# 인증 관련 함수 임포트 (비밀번호 해싱 및 검증)
from app.stimuli.functions.auth import AuthFunction
from app.stimuli.dtos.user_dto import UserResponse
from app.stimuli.functions.tokening import get_current_user_id
from app.models.users import UserModel

# Tortoise ORM 예외 임포트

router = APIRouter(prefix="/register", tags=["Register"])
templates = Jinja2Templates(
    directory="app/stimuli/channels"
)  # 템플릿 경로 유지 (필요 시 조정)


@router.post("/register", response_model=UserResponse)
async def register(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...),
):
    if password != confirm_password:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "비밀번호가 일치하지 않습니다."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    existing_user = await UserModel.filter(email=email).first()
    if existing_user:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "이미 존재하는 이메일입니다."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    hashed_password = AuthFunction.set_password(password)

    user = await UserModel.create(
        name=name,
        email=email,
        password=hashed_password,  #
    )
    return RedirectResponse(url="../dashboard", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/me", response_model=UserResponse)
async def read_users_me(current_user_id: int = Depends(get_current_user_id)):
    user = await UserModel.get_or_none(id=current_user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return UserResponse.model_validate(user)
