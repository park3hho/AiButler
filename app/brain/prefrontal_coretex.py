import os
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx
from dotenv import load_dotenv
from app.brain.dtos.external_stimuli_dto import SendStimuli
import google.generativeai as genai  # ← 올바른 import
router = APIRouter()

load_dotenv()  # .env 파일에서 환경변수 로드
ego = os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 환경변수로 API 키 저장 권장
model = genai.GenerativeModel("gemini-1.5-pro")
genai.configure(api_key=GEMINI_API_KEY)
templates = Jinja2Templates(directory="app/stimuli/channels")


@router.get("/", response_class=HTMLResponse)
def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/accept_external_stimuli", response_class=HTMLResponse)
async def ask_question(request: Request, stimuli: str = Form(...)):
    response = model.generate_content(stimuli)  # 핵심 호출
    answer = response.text  # 응답에서 텍스트 추출

    print("Gemini 답변:", answer)

    return templates.TemplateResponse("index.html", {"request": request, "answer": answer})
