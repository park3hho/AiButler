import cv2
import time
# 0은 기본 카메라 (내장 웹캠) 의미. 외부 장치면 1, 2 등으로 바꿔보세요.

VIDEO_PATH = "app/eyes/visual_stimulus_samples/sv.mp4"

def gen_frames():
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print("❌ 동영상 열기 실패")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    speed_factor = 2  # 2배 느리게
    delay = (1 / fps) / speed_factor

    while True:
        success, frame = cap.read()
        if not success:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 영상 끝나면 처음으로
            continue

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        time.sleep(delay)  # 🔸 프레임 사이에 딜레이 추가
 # 열려있는 모든 창 닫기
