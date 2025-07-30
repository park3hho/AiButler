from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from app.eyes.occipital_lobe import gen_frames  # 비디오 스트림 함수 임포트
# JWT 토큰 검증 관련 함수 임포트
from app.stimuli.functions.tokening import get_current_user_id
router = APIRouter(prefix="", tags=["Home"])
templates = Jinja2Templates(directory="app/stimuli/channels")

@router.get("/")
def index(request: Request):
    """
    메인 페이지를 렌더링합니다.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/register")
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/video_feed")
def video_feed():
    """
    비디오 스트림을 제공합니다.
    """
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")


@router.get('/dashboard', response_class=HTMLResponse) # HTML 응답임을 명시
async def dashboard_page(
    request: Request,
    # Depends를 사용하여 get_current_user_id 함수를 호출하고 그 결과를 user_id에 주입
    # get_current_user_id에서 HTTPException이 발생하면 바로 클라이언트에게 반환됨
    user_id: str = Depends(get_current_user_id)
):
    """
    대시보드 페이지를 렌더링합니다.
    사용자가 로그인되어 있지 않거나 토큰이 유효하지 않으면 401 Unauthorized 오류를 반환합니다.
    """
    # user_id가 성공적으로 주입되었다면, 사용자는 로그인된 상태입니다.
    # user_id를 템플릿으로 넘겨주어 활용할 수도 있습니다.
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "user_id": user_id} # user_id를 템플릿에 전달
    )

