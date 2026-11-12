# 🎯 나만의 파이썬 퀴즈 게임 (Python Console Quiz Game)

## 📌 1. 프로젝트 개요
- Python 기본 문법과 객체 지향(클래스)을 활용하여 터미널에서 동작하는 콘솔 기반 퀴즈 게임입니다.
- `state.json` 파일을 통해 프로그램을 종료해도 퀴즈 데이터와 최고 점수가 유지되는 **데이터 영속성**을 구현했습니다.
- `try/except`를 활용한 강력한 예외 처리와 Git 브랜치 전략, GitHub 협업 워크플로우를 실습합니다.

### 💡 퀴즈 주제 선정 이유
- **주제:** 파이썬 및 IT 개발 기초 상식
- **선정 이유:** 프로그래밍 입학 연수 과정에서 학습한 핵심 개념들을 직접 퀴즈 문제로 출제하고 풀어봄으로써, 지식을 자연스럽게 복습하고 콘솔 응용 프로그램 구조를 체득하기 위해 이 주제를 선정했습니다.

---

## 💻 2. 실행 환경
| 항목 | 환경 |
|------|------|
| OS | Windows 11 |
| 터미널 | VS Code Terminal / PowerShell |
| 언어 | Python 3.12.8 |
| 데이터 저장 | JSON (`state.json`, UTF-8) |
| 버전 관리 | Git 2.56.0.windows.4 / GitHub |

---

## 🚀 3. 실행 방법
프로젝트 루트 폴더에서 터미널을 열고 아래 명령어를 입력하여 실행합니다.

```powershell
python main.py
```

---

## 🛠️ 4. 기능 목록
1. **퀴즈 풀기:** 저장된 퀴즈를 순서대로 풀고 정답 여부 확인 및 최종 점수 산출 (최고 점수 자동 갱신)
2. **퀴즈 추가:** 새로운 문제, 4개의 선택지, 정답 번호를 입력받아 즉시 `state.json`에 저장
3. **퀴즈 목록:** 현재 등록된 모든 퀴즈 목록 조회
4. **점수 확인:** 역대 최고 점수 및 정답 개수 확인
5. **안전한 예외/오류 처리:** 잘못된 숫자 입력, 빈 값, 문자 입력, 파일 손상 시 안내 및 안전 종료(`Ctrl+C` 대응) 지원

---

## 📂 5. 파일 구조 및 데이터 파일 설명

### 파일 구조
```text
quiz-game/
├── .gitignore         # Git 추적 제외 설정 (__pycache__, venv 등)
├── README.md          # 프로젝트 설명서 및 실행 기록
├── state.json         # 퀴즈 데이터 및 최고 점수 저장 파일 (자동 생성/관리)
└── main.py            # 프로그램 실행 및 게임 로직 진입점
```

### 데이터 파일 (`state.json`) 설명
- **경로:** 프로젝트 루트 (`./state.json`)
- **역할:** 프로그램 종료 후에도 퀴즈 목록과 최고 점수를 보존하는 영속성 저장소 (UTF-8 인코딩)
- **최소 스키마 구조:**
  ```json
  {
      "quizzes": [
          {
              "question": "문제 내용",
              "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],
              "answer": 1
          }
      ],
      "best_score": 0
  }
  ```

---

## ✅ 6. 수행 항목 체크리스트
- [x] GitHub 저장소 생성 및 로컬 연결
- [x] .gitignore, README.md 작성
- [x] 초기 설정 후 첫 commit / push 수행
- [ ] 메뉴 출력 및 기능 선택 구현
- [ ] 잘못된 입력 / 예외 처리 구현
- [ ] Quiz 클래스 정의 (question, choices, answer)
- [ ] 기본 퀴즈 데이터 5개 이상 작성
- [ ] 퀴즈 풀기 기능 (브랜치 생성 후 작업 → 병합)
- [ ] 퀴즈 추가 기능 및 파일 저장
- [ ] 퀴즈 목록 확인 기능
- [ ] 점수 확인 및 최고 점수 갱신·저장
- [ ] state.json 영속성 검증 (재실행 후 데이터 유지)
- [ ] 파일 없음 / 손상 시 복구 처리
- [ ] 10개 이상 의미 있는 커밋
- [ ] 브랜치 생성·병합 1회 이상
- [ ] clone, pull 각 1회 이상
- [x] README.md 필수 항목 모두 작성

---

## 📜 7. 초기 설정 및 Git 커밋 로그 (수행 내용)

### ① 프로젝트 폴더 초기화 및 설정 파일 생성
```powershell
PS C:\Users\jockersmile1176\Documents\Workspace> python --version
Python 3.12.8
PS C:\Users\jockersmile1176\Documents\Workspace> git --version
git version 2.56.0.windows.4
PS C:\Users\jockersmile1176\Documents\Workspace> mkdir quiz-game
PS C:\Users\jockersmile1176\Documents\Workspace> cd quiz-game
```

### ② Git 초기화 및 원격 저장소 연결
```powershell
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git init
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git remote add origin [https://github.com/jokersmile86/1-2quizgame.git](https://github.com/jokersmile86/1-2quizgame.git) 
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git remote -v
origin  [https://github.com/jokersmile86/1-2quizgame.git](https://github.com/jokersmile86/1-2quizgame.git) (fetch)
origin  [https://github.com/jokersmile86/1-2quizgame.git](https://github.com/jokersmile86/1-2quizgame.git) (push)
```

### ③ 설정 파일 생성 및 첫 커밋/푸시 수행
```powershell
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> New-Item .gitignore -ItemType File
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> New-Item README.md -ItemType File
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git add .
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git commit -m "Chore: 프로젝트 초기 설정 및 기본 파일 생성"
[main (root-commit) 3ed5d89] Chore: 프로젝트 초기 설정 및 기본 파일 생성
 2 files changed, 10 insertions(+)

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git push -u origin main
To [https://github.com/jokersmile86/1-2quizgame.git](https://github.com/jokersmile86/1-2quizgame.git)
 * [new branch]      main -> main
```