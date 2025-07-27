import os
import httpx
import google.generativeai as genai  # ← 올바른 import
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from app.eyes.functions.accept_visual_stimuli import accept_visual_stimuli
from app.brain.functions.process_images import process_image
from app.brain.functions.exposure_opinion import basic_prompt
from app.brain.functions.parse_ingredients import parse_ingredients
router = APIRouter()
load_dotenv()  # .env 파일에서 환경변수 로드
ego = os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 환경변수로 API 키 저장 권장
model = genai.GenerativeModel("gemini-1.5-pro")
genai.configure(api_key=GEMINI_API_KEY)
templates = Jinja2Templates(directory="app/stimuli/channels")

@router.post("/accept_textual_stimuli", response_class=HTMLResponse) # Response
async def answer_question(request: Request, stimuli: str = Form(...)):
    
    # 영상 -> 이미지 바이트 리스트
    video_frames = accept_visual_stimuli("app/eyes/visual_stimulus_samples/sv.mp4", 1)
    processed_image = process_image(video_frames) # 바이트화 한 다음 넘겨야 답변이 정확하네
  # 텍스트 + 이미지 바이트 리스트 → 하나의 메시지 리스트로 구성
    multimodal_input = basic_prompt + [stimuli] + processed_image # 첫 번째 요소는 텍스트
    response = model.generate_content(multimodal_input)
    answer = response.text  # 응답에서 텍스트 추출

    print("frame 수:",len(video_frames))
    print("사용자 답변:", stimuli)
    print("Gemini 답변:", answer)
    print(parse_ingredients(answer))

    return templates.TemplateResponse("index.html", {"request": request, "answer": answer})


