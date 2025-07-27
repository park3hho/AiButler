from google.ai import generativelanguage as genai


async def exposure_opinion(external_stimuli):
    # 예) prompt 만들기
    prompt = genai.types.TextPrompt(text="안녕, 오늘 날씨 어때?")

    # 모델 객체 준비 (생략 - 이미 준비된 상태라고 가정)
    #model = client.get_model("gemini-1")

    # API 호출
    response: genai.types.GenerateContentResponse = model.generate_content(prompt=prompt)

    # 실제 답변 텍스트 얻기
    answer = response.candidates[0].content

    print("Gemini 답변:", answer)
