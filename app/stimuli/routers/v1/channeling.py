from fastapi import APIRouter, Response, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from app.eyes.occipital_lobe import gen_frames  # 함수 임포트


router = APIRouter()
templates = Jinja2Templates(directory="app/stimuli/channels")

@router.get("/video_feed")
def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@router.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})