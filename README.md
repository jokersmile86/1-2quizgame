# 🎯 나만의 파이썬 퀴즈 게임 (Python Console Quiz Game)

## 📌 1. 프로젝트 개요

-   Python 기본 문법과 객체 지향(클래스)을 활용하여 터미널에서 동작하는
    콘솔 기반 퀴즈 게임입니다.
-   `state.json` 파일을 통해 프로그램을 종료해도 퀴즈 데이터와 최고
    점수가 유지되는 **데이터 영속성**을 구현했습니다.
-   `try/except`를 활용한 강력한 예외 처리와 Git 브랜치 전략, GitHub
    협업 워크플로우를 실습합니다.

### 💡 퀴즈 주제 선정 이유

-   **주제:** 파이썬 및 IT 개발 기초 상식
-   **선정 이유:** 프로그래밍 입학 연수 과정에서 학습한 핵심 개념들을
    직접 퀴즈 문제로 출제하고 풀어봄으로써, 지식을 자연스럽게 복습하고
    콘솔 응용 프로그램 구조를 체득하기 위해 이 주제를 선정했습니다.

------------------------------------------------------------------------

## 💻 2. 실행 환경

  항목          환경
  ------------- -------------------------------
  OS            Windows 11
  터미널        VS Code Terminal / PowerShell
  언어          Python 3.12.8
  데이터 저장   JSON (`state.json`, UTF-8)
  버전 관리     Git 2.56.0.windows.4 / GitHub

------------------------------------------------------------------------

## 🚀 3. 실행 방법

프로젝트 루트 폴더에서 터미널을 열고 아래 명령어를 입력하여 실행합니다.

``` powershell
python main.py
```

------------------------------------------------------------------------

## 🛠️ 4. 기능 목록

1.  **퀴즈 풀기:** 저장된 퀴즈를 순서대로 풀고 정답 여부 확인 및 최종
    점수 산출 (최고 점수 자동 갱신)
2.  **퀴즈 추가:** 새로운 문제, 4개의 선택지, 정답 번호를 입력받아 즉시
    `state.json`에 저장
3.  **퀴즈 목록:** 현재 등록된 모든 퀴즈 목록 조회
4.  **점수 확인:** 역대 최고 점수 및 정답 개수 확인
5.  **안전한 예외/오류 처리:** 잘못된 숫자 입력, 빈 값, 문자 입력, 파일
    손상 시 안내 및 안전 종료(`Ctrl+C` 대응) 지원

-   **Tip:** `state.json` 파일이 자동 생성되므로 언제든 이어서 학습할 수
    있습니다.

------------------------------------------------------------------------

## 📂 5. 파일 구조 및 데이터 파일 설명

### 파일 구조

``` text
quiz-game/
├── .gitignore         # Git 추적 제외 설정 (__pycache__, venv 등)
├── README.md          # 프로젝트 설명서 및 실행 기록
├── state.json         # 퀴즈 데이터 및 최고 점수 저장 파일 (자동 생성/관리)
└── main.py            # 프로그램 실행 및 게임 로직 진입점
```

-   **Tip:** UTF-8 인코딩을 사용하여 한글이 깨지지 않고 안전하게
    저장됩니다.

### 데이터 파일 (`state.json`) 설명

-   **경로:** 프로젝트 루트 (`./state.json`)

-   **역할:** 프로그램 종료 후에도 퀴즈 목록과 최고 점수를 보존하는
    영속성 저장소 (UTF-8 인코딩)

-   **최소 스키마 구조:**

    ``` json
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

------------------------------------------------------------------------

## ✅ 6. 수행 항목 체크리스트

-   [x] GitHub 저장소 생성 및 로컬 연결
-   [x] .gitignore, README.md 작성
-   [x] 초기 설정 후 첫 commit / push 수행
-   [x] 메뉴 출력 및 기능 선택 구현
-   [x] 잘못된 입력 / 예외 처리 구현
-   [x] Quiz 클래스 정의 (question, choices, answer)
-   [x] 기본 퀴즈 데이터 5개 이상 작성 (총 10개 구성 완료)
-   [x] 퀴즈 풀기 기능 (브랜치 생성 후 작업 → 병합)
-   [x] 퀴즈 추가 기능 및 파일 저장
-   [x] 퀴즈 목록 확인 기능
-   [x] 점수 확인 및 최고 점수 갱신·저장
-   [x] state.json 영속성 검증 (재실행 후 데이터 유지)
-   [x] 파일 없음 / 손상 시 복구 처리
-   [x] 10개 이상 의미 있는 커밋 완료
-   [x] 브랜치 생성·병합 1회 이상 완료
-   [x] clone, pull 각 1회 이상 완료
-   [x] README.md 필수 항목 모두 작성

------------------------------------------------------------------------

## 📜 7. 단계별 수행 내용 및 실행 로그

### ① 프로젝트 폴더 초기화 및 GitHub 원격 저장소 연결

``` powershell
PS C:\Users\jockersmile1176\Documents\Workspace> python --version
Python 3.12.8
PS C:\Users\jockersmile1176\Documents\Workspace> git --version
git version 2.56.0.windows.4
PS C:\Users\jockersmile1176\Documents\Workspace> mkdir quiz-game
PS C:\Users\jockersmile1176\Documents\Workspace> cd quiz-game

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git init
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git remote add origin https://github.com/jokersmile86/1-2quizgame.git 
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git remote -v
origin  https://github.com/jokersmile86/1-2quizgame.git (fetch)
origin  https://github.com/jokersmile86/1-2quizgame.git (push)
```

### ② 설정 파일 생성 및 첫 커밋/푸시 수행 (커밋 #1)

``` powershell
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> New-Item .gitignore -ItemType File
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> New-Item README.md -ItemType File
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git add .
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git commit -m "Chore: 프로젝트 초기 설정 및 기본 파일 생성"
[main (root-commit) 3ed5d89] Chore: 프로젝트 초기 설정 및 기본 파일 생성
 2 files changed, 10 insertions(+)

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git push -u origin main
To https://github.com/jokersmile86/1-2quizgame.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

### ③ 핵심 로직(`main.py`) 구현 및 퀴즈 풀이/예외 처리 검증 (커밋 #2)

-   `state.json` 미존재 시 기본 데이터(5문제) 자동 생성 검증
-   퀴즈 5문제 풀이 후 점수 산출 및 최고 점수 갱신(`3점`) 확인
-   잘못된 입력(`ㅁ`, `a`, `9`)에 대한 예외 처리 안내 메시지 동작 검증

``` powershell
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> python main.py
📂 state.json 파일이 없어 기본 데이터로 생성합니다.
========================================
        🎯 나만의 퀴즈 게임 🎯        
📂 저장된 데이터 로드 완료 (퀴즈 5개, 최고점수: 0점)
========================================

1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1

📝 퀴즈를 시작합니다! (총 5문제)
... (중략) ...
========================================
🏆 결과: 총 5문제 중 3문제 정답!
🎉 새로운 최고 점수입니다!
========================================

선택: 4
🏆 최고 점수: 3점

선택: ㅁ
⚠️ 숫자 형태만 입력 가능합니다.
선택: a
⚠️ 숫자 형태만 입력 가능합니다.
선택: 9
⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.
선택: 5
👋 프로그램을 종료합니다. 이용해 주셔서 감사합니다!

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git add main.py
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git commit -m "Feat: Quiz 및 QuizGame 클래스, 예외 처리, 파일 영속성 구현"
[main 9e29fb9] Feat: Quiz 및 QuizGame 클래스, 예외 처리, 파일 영속성 구현
 1 file changed, 234 insertions(+)
 create mode 100644 main.py
```

### ④ 작업 브랜치 생성 및 퀴즈 5개 추가·목록 조회 검증 (커밋 #3)

-   `feature/quiz-features` 브랜치 생성 및 전환
-   재실행 시 기존 `state.json` 데이터(5문제, 최고점수 3점) 유지 확인
-   퀴즈 5개를 추가 등록하여 총 10문제 목록 조회 및 저장 검증
-   `.gitignore` 예외 처리를 위해 `git add -f state.json`으로 데이터
    파일 추적 반영

``` powershell
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git checkout -b feature/quiz-features
Switched to a new branch 'feature/quiz-features'
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> python main.py
========================================
        🎯 나만의 퀴즈 게임 🎯        
📂 저장된 데이터 로드 완료 (퀴즈 5개, 최고점수: 3점)
========================================
... (퀴즈 5개 추가 진행) ...
선택: 3

📋 등록된 퀴즈 목록 (총 10개)
----------------------------------------
[1] Python에서 리스트(List)의 특징으로 알맞은 것은?
[2] 다음 중 파이썬의 기본 데이터 타입이 아닌 것은?
[3] 깃(Git)에서 로컬 저장소의 변경 이력을 원격 저장소에 업로드하는 명령어는?
[4] 다음 중 파일 권한 '644'에서 소유자(Owner)가 가진 권한으로 올바른 것은?
[5] Docker 컨테이너를 실행할 때 포트를 매핑하기 위해 사용하는 옵션은?
[6] 파이썬에서 함수의 반환값을 지정할 때 사용하는 키워드는?
[7] Git에서 새로운 브랜치를 생성하고 동시에 해당 브랜치로 이동하는 명령어는?
[8] 실행 중인 모든 Docker 컨테이너의 목록을 확인할 수 있는 명령어는?
[9] 리눅스에서 파일 소유자에게는 읽기·쓰기·실행, 그룹과 기타 사용자에게는 읽기·실행 권한을 부여하는 숫자 표현은?
[10] 파이썬에서 예외 처리를 위해 사용하는 블록의 키워드가 아닌 것은?
----------------------------------------
선택: 5
👋 프로그램을 종료합니다. 이용해 주셔서 감사합니다!

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git add -f state.json
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git add README.md
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git commit -m "Feat: 퀴즈 데이터(state.json) 및 README 문서 업데이트"
[feature/quiz-features e73b1f3] Feat: 퀴즈 데이터(state.json) 및 README 문서 업데이트
 2 files changed, 232 insertions(+)
 create mode 100644 state.json
```

### 10번째 커밋 로그 (README 참고용)

PS
C:`\Users`{=tex}`\jockersmile1176`{=tex}`\Documents`{=tex}`\Workspace`{=tex}`\quiz`{=tex}-game\>
git add README.md PS
C:`\Users`{=tex}`\jockersmile1176`{=tex}`\Documents`{=tex}`\Workspace`{=tex}`\quiz`{=tex}-game\>
git commit -m "Docs: README.md 최종 수정 및 문서 정돈 완료"
\[feature/quiz-features a83f2c5\] Docs: README.md 최종 수정 및 문서 정돈
완료 1 file changed, 10 insertions(+), 9 deletions(-) PS
C:`\Users`{=tex}`\jockersmile1176`{=tex}`\Documents`{=tex}`\Workspace`{=tex}`\quiz`{=tex}-game\>
git rev-list --count HEAD 10

## 📌 8. Git Clone 및 Pull 실습

-   GitHub 원격 저장소를 별도 폴더에 Clone하여 프로젝트 복제 확인
-   Clone한 저장소에서 main 브랜치 및 프로젝트 파일 확인
-   원격 저장소의 변경 사항을 Pull하여 로컬 저장소에 반영하는 실습 진행

### ⑤ 작업 브랜치 Push 및 병합 과정

-   `feature/quiz-features` 브랜치의 작업 내용을 원격 저장소에 Push
-   처음 `main` 브랜치로 이동하려 했으나, 커밋하지 않은 `README.md` 변경
    사항이 있어 checkout이 중단됨
-   당시 feature 브랜치에서 자기 자신을 병합하여 `Already up to date`가
    출력됨
-   이후 README 변경 사항을 커밋한 뒤 `main`으로 이동하여 정상적으로
    병합 진행

``` powershell
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git push origin feature/quiz-features
Enumerating objects: 30, done.
Counting objects: 100% (30/30), done.
Delta compression using up to 24 threads
Compressing objects: 100% (28/28), done.
Writing objects: 100% (28/28), 11.23 KiB | 2.81 MiB/s, done.
Total 28 (delta 14), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (14/14), done.
remote:
remote: Create a pull request for 'feature/quiz-features' on GitHub by visiting:
remote:      https://github.com/jokersmile86/1-2quizgame/pull/new/feature/quiz-features
remote:
To https://github.com/jokersmile86/1-2quizgame.git
 * [new branch]      feature/quiz-features -> feature/quiz-features

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git checkout main
error: Your local changes to the following files would be overwritten by checkout:
        README.md
Please commit your changes or stash them before you switch branches.
Aborting

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git merge feature/quiz-features
Already up to date.

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git push origin main
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/jokersmile86/1-2quizgame.git
   3ed5d89..9e29fb9  main -> main
```

위 로그에서 `git checkout main`은 실패했으므로, 그 시점에는 feature
브랜치에 그대로 남아 있었습니다. 따라서 이어서 실행한
`git merge feature/quiz-features`는 실제 main 병합이 아니었습니다.

### ⑥ README 변경사항 커밋 후 main 병합 및 Push

-   `README.md` 변경사항을 feature 브랜치에서 커밋하여 작업 트리를 정리
-   `main` 브랜치로 이동하고 원격 main을 Pull
-   `feature/quiz-features`를 main에 병합
-   병합 결과 `Fast-forward`가 확인되었으며, `README.md`, `main.py`,
    `state.json`이 main에 반영됨
-   최종 main 브랜치를 GitHub 원격 저장소에 Push

``` powershell
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git add README.md
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git commit -m "Docs: README.md 변경사항 임시 보관"
[feature/quiz-features 8b0d3a7] Docs: README.md 변경사항 임시 보관
 1 file changed, 9 insertions(+), 1 deletion(-)

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git pull origin main
From https://github.com/jokersmile86/1-2quizgame
 * branch            main       -> FETCH_HEAD
Already up to date.

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git merge feature/quiz-features
Updating 9e29fb9..8b0d3a7
Fast-forward
 README.md  | 223 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 main.py    |  51 +++++++++++---
 state.json | 105 +++++++++++++++++++++++++++++
 3 files changed, 369 insertions(+), 10 deletions(-)
 create mode 100644 state.json

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 24 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 534 bytes | 534.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 2), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/jokersmile86/1-2quizgame.git
   9e29fb9..8b0d3a7  main -> main
```

### ⑦ Clone 실습

-   기존 작업 폴더(`quiz-game`)와 별도의 폴더(`1-2quizgame`)에 GitHub
    원격 저장소를 복제
-   복제된 저장소에서 `main` 브랜치 및 프로젝트 파일 확인
-   `.gitignore`, `main.py`, `README.md`, `state.json` 파일이 존재하는
    것을 확인

``` powershell
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> cd ..
PS C:\Users\jockersmile1176\Documents\Workspace> git clone https://github.com/jokersmile86/1-2quizgame.git
Cloning into '1-2quizgame'...
remote: Enumerating objects: 35, done.
remote: Counting objects: 100% (35/35), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 35 (delta 17), reused 34 (delta 16), pack-reused 0 (from 0)
Receiving objects: 100% (35/35), done.
Resolving deltas: 100% (17/17), done.

PS C:\Users\jockersmile1176\Documents\Workspace> cd 1-2quizgame
PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> git branch
* main

PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> dir

    디렉터리: C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----      2026-11-12   오후 2:45            173 .gitignore
-a----      2026-11-12   오후 2:45          11179 main.py
-a----      2026-11-12   오후 2:45          10633 README.md
-a----      2026-11-12   오후 2:45           3436 state.json
```

### ⑧ Pull 실습

-   기존 작업 폴더에서 `README.md`에 Clone 및 Pull 실습 내용을 추가
-   변경 내용을 커밋하고 원격 `main` 브랜치에 Push
-   별도로 Clone한 저장소에서 `git pull origin main`을 실행하여 원격
    변경 사항을 내려받음
-   `Fast-forward` 및 최신 커밋 해시 `a216451`을 확인하여 Pull 성공 검증

``` powershell
PS C:\Users\jockersmile1176\Documents\Workspace> cd 1-2quizgame
PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> git branch
* main

PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> dir

    디렉터리: C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----      2026-11-12   오후 2:45            173 .gitignore
-a----      2026-11-12   오후 2:45          11179 main.py
-a----      2026-11-12   오후 2:45          10633 README.md
-a----      2026-11-12   오후 2:45           3436 state.json

PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> cd ..\quiz-game
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git branch
  feature/quiz-features
* main

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git add README.md
PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git commit -m "Docs: Git clone 및 pull 실습 내용 추가"
[main a216451] Docs: Git clone 및 pull 실습 내용 추가
 1 file changed, 6 insertions(+), 1 deletion(-)

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 24 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 551 bytes | 551.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/jokersmile86/1-2quizgame.git
   8b0d3a7..a216451  main -> main

PS C:\Users\jockersmile1176\Documents\Workspace\quiz-game> cd ..\1-2quizgame
PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> git branch
* main

PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> git pull origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 531 bytes | 40.00 KiB/s, done.
From https://github.com/jokersmile86/1-2quizgame
 * branch            main       -> FETCH_HEAD
   8b0d3a7..a216451  main       -> origin/main
Updating 8b0d3a7..a216451
Fast-forward
 README.md | 7 ++++++-
 1 file changed, 6 insertions(+), 1 deletion(-)

PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> git log -1 --oneline
a216451 (HEAD -> main, origin/main, origin/HEAD) Docs: Git clone 및 pull 실습 내용 추가

PS C:\Users\jockersmile1176\Documents\Workspace\1-2quizgame> notepad README.md
```

### ⑨ Clone 및 Pull 최종 검증 결과

  항목                                  결과
  ------------------------------------- ------
  원격 저장소 Clone                     완료
  Clone 저장소의 main 브랜치 확인       완료
  프로젝트 파일 확인                    완료
  원본 저장소에서 README 변경 및 Push   완료
  Clone 저장소에서 Pull                 완료
  최신 커밋 `a216451` 확인              완료

-   `git clone`: 원격 저장소 전체를 새로운 로컬 폴더에 복제하는 작업임을
    확인했습니다.
-   `git pull`: 원격 저장소의 최신 변경 이력을 가져와 현재 로컬 브랜치에
    반영하는 작업임을 확인했습니다.
-   기존 작업 폴더와 Clone 폴더를 별도로 사용하여 원격 저장소를 통한
    변경 사항 동기화 과정을 검증했습니다.
