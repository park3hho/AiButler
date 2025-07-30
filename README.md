## 자주 쓸 명령어
docker compose up -d
docker compose exec ai-butler bash
docker stop $(docker ps -q)



## ToDoList
1. 카메라 연결
2. API와 실시간 연결(토큰 너무 잡아먹으니 테스트에선 Long-term)
3. 토큰으로 로그인 확인
4. 사용자가 확인하고 데이터 베이스에 집어넣기

```
AiButler/
├── app/
├── main.py
├── README.md
└── .gitignore
```

## 🔧 1일차 250726
1. 🔧 docker-compose 기본 설정
2. 🔧 github Actions: docker image build-push 자동화
3. 🔧 git-message 템플릿 제작
4. 🔧 Actions Code Fix
5. 🔧 Linting

## ✨ 2일차 250727
1. ✨ HTML 생성
2. ✨ INPUT BOX를 사용한 AI와 대화
3. ✨ 이미지
4. ♻️ 파일 구조 수정
5. ⬆️ 개많이 깜

## ✨ 3일차 250728
1. ✨ 동영상 인식 -> 답변 반환
2. ✨ 답변 고정화 및 jsonify
3. ⬆️ Database 연동 성공
4. ⬆️ ERD 생성
5. ✨ 이미지 처리 기능

## ✨ 4일차 250729
- / 

## ✨ 5일차 250730
1. ✨ 메인페이지에 토큰 인증 구현