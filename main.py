import json
import os
import sys

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question       # 문제
        self.choices = choices         # 선택지 4개 리스트
        self.answer = answer           # 정답 번호 (1~4)

    def display(self):
        print(f"\n----------------------------------------")
        print(f"{self.question}")
        for idx, choice in enumerate(self.choices, 1):
            print(f"  {idx}. {choice}")
        print(f"----------------------------------------")

    def check_answer(self, user_answer):
        return self.answer == user_answer


class QuizGame:
    def __init__(self):
        self.filename = "state.json"
        self.data = self.load_data()
        self.quizzes = []
        self.load_quizzes_to_objects()

    def load_data(self):
        """state.json 파일 로드, 없거나 손상 시 기본 데이터 반환 및 복구"""
        default_data = {
            "quizzes": [
                {
                    "question": "Python에서 리스트(List)의 특징으로 알맞은 것은?",
                    "choices": ["순서가 없고 중복이 안 된다", "순서가 있고 수정이 가능하다", "값을 변경할 수 없다", "키와 값으로 이루어져 있다"],
                    "answer": 2
                },
                {
                    "question": "다음 중 파이썬의 기본 데이터 타입이 아닌 것은?",
                    "choices": ["int", "str", "array", "bool"],
                    "answer": 3
                },
                {
                    "question": "깃(Git)에서 로컬 저장소의 변경 이력을 원격 저장소에 업로드하는 명령어는?",
                    "choices": ["git pull", "git push", "git clone", "git commit"],
                    "answer": 2
                },
                {
                    "question": "다음 중 파일 권한 '644'에서 소유자(Owner)가 가진 권한으로 올바른 것은?",
                    "choices": ["읽기 전용", "읽기 및 쓰기", "읽기, 쓰기, 실행", "실행 전용"],
                    "answer": 2
                },
                {
                    "question": "Docker 컨테이너를 실행할 때 포트를 매핑하기 위해 사용하는 옵션은?",
                    "choices": ["-v", "-d", "-p", "-t"],
                    "answer": 3
                }
            ],
            "best_score": 0
        }

        if not os.path.exists(self.filename):
            print("📂 state.json 파일이 없어 기본 데이터로 생성합니다.")
            self.save_data(default_data)
            return default_data

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "quizzes" not in data or "best_score" not in data:
                    raise ValueError("데이터 키값이 누락되었습니다.")
                return data
        except (json.JSONDecodeError, ValueError) as e:
            print(f"⚠️ 경고: 데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다. ({e})")
            self.save_data(default_data)
            return default_data
        except Exception as e:
            print(f"⚠️ 파일 읽기 오류 발생: {e}. 기본 데이터를 사용합니다.")
            return default_data

    def save_data(self, data=None):
        """데이터를 state.json에 저장"""
        if data is None:
            # Quiz 객체 리스트를 다시 딕셔너리 형태로 변환하여 저장
            quizzes_list = [
                {
                    "question": q.question,
                    "choices": q.choices,
                    "answer": q.answer
                }
                for q in self.quizzes
            ]
            data = {
                "quizzes": quizzes_list,
                "best_score": self.data.get("best_score", 0)
            }
        
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"⚠️ 데이터 저장 실패: {e}")

    def load_quizzes_to_objects(self):
        """딕셔너리 형태의 퀴즈 데이터를 Quiz 객체로 변환"""
        self.quizzes = []
        for q_dict in self.data.get("quizzes", []):
            self.quizzes.append(
                Quiz(q_dict["question"], q_dict["choices"], q_dict["answer"])
            )

    def get_validated_input(self, prompt, min_val, max_val):
        """공백 제거, 숫자 변환 실패, 범위 초과, 빈 입력 및 안전 종료 처리"""
        while True:
            try:
                user_input = input(prompt).strip()
                if not user_input:
                    print("⚠️ 빈 값은 입력할 수 없습니다. 다시 시도해주세요.")
                    continue
                
                number = int(user_input)
                if min_val <= number <= max_val:
                    return number
                else:
                    print(f"⚠️ 잘못된 입력입니다. {min_val}~{max_val} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("⚠️ 숫자 형태만 입력 가능합니다.")
            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️ 프로그램을 안전하게 종료합니다.")
                self.save_data()
                sys.exit(0)

    def run(self):
        print("========================================")
        print("        🎯 나만의 퀴즈 게임 🎯        ")
        print(f"📂 저장된 데이터 로드 완료 (퀴즈 {len(self.quizzes)}개, 최고점수: {self.data.get('best_score', 0)}점)")
        print("========================================")

        while True:
            print("\n1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("========================================")
            
            choice = self.get_validated_input("선택: ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("👋 프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
                break

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요!")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0

        for idx, q in enumerate(self.quizzes, 1):
            print(f"\n[문제 {idx}/{len(self.quizzes)}]")
            q.display()
            user_ans = self.get_validated_input("정답 입력 (1-4): ", 1, 4)

            if q.check_answer(user_ans):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {q.answer}번입니다.")

        print(f"\n========================================")
        print(f"🏆 결과: 총 {len(self.quizzes)}문제 중 {score}문제 정답!")
        
        current_best = self.data.get("best_score", 0)
        if score > current_best:
            self.data["best_score"] = score
            self.save_data()
            print("🎉 새로운 최고 점수입니다!")
        print("========================================")

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        try:
            question = input("문제를 입력하세요: ").strip()
            if not question:
                print("⚠️ 빈 문제는 추가할 수 없습니다.")
                return

            choices = []
            for i in range(1, 5):
                choice = input(f"선택지 {i}: ").strip()
                if not choice:
                    print("⚠️ 빈 선택지는 입력할 수 없습니다.")
                    return
                choices.append(choice)

            answer = self.get_validated_input("정답 번호 (1-4): ", 1, 4)

            # 새 퀴즈 추가
            new_quiz = Quiz(question, choices, answer)
            self.quizzes.append(new_quiz)
            self.save_data()
            print("✅ 퀴즈가 성공적으로 추가되어 저장되었습니다!")
        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 입력을 취소합니다.")

    def show_quizzes(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for idx, q in enumerate(self.quizzes, 1):
            print(f"[{idx}] {q.question}")
        print("-" * 40)

    def show_score(self):
        best = self.data.get("best_score", 0)
        print(f"\n🏆 최고 점수: {best}점")


if __name__ == "__main__":
    game = QuizGame()
    game.run()