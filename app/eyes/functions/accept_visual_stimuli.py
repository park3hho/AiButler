import cv2
import io
from PIL import Image


def accept_visual_stimuli(video_path, frame_rate):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_number = 0
    keyframes = []  # 이미지 바이트화된 것을 담을 리스트

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if int(frame_number % (fps * frame_rate)) == 0:
            # OpenCV는 BGR, PIL은 RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb_frame)

            # 메모리에서 이미지 바이트로 변환 (예: JPEG)
            buffer = io.BytesIO()
            pil_img.save(buffer, format="JPEG")
            buffer.seek(0)
            keyframes.append(buffer.read())  # 바이트 데이터 저장

        frame_number += 1

    cap.release()
    return keyframes  # 이미지 바이트 리스트
