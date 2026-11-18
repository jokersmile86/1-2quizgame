"""
=========================================================
프로젝트 이름: 나만의 파이썬 퀴즈 게임 (Python Console Quiz Game)
설명: 객체 지향(OOP) 구조와 JSON 파일 영속성, 그리고 강력한 예외 처리를
      적용한 터미널 기반 퀴즈 게임 프로그램입니다.
      (자동 백업/복구, 권한 오류 처리, 대량 데이터 페이징 포함)
=========================================================
"""

import json
import os
import random
import shutil
import sys

# ---------------------------------------------------------
# 요구사항 변경 시 가장 먼저 수정하는 설정값 (README 8장 '영향도 가이드' 참고)
# ---------------------------------------------------------
NUM_CHOICES = 4        # 선택지 개수 (5지선다로 바꾸려면 5)
DEFAULT_POINTS = 1     # 문항 기본 배점 (가중치 채점 시 문항별로 다르게 지정)
PAGE_SIZE = 20         # 퀴즈 목록 한 페이지에 보여줄 개수 (대량 데이터 대응)
SHUFFLE_QUIZZES = True # 퀴즈 풀기 시 문제 순서를 랜덤으로 섞을지 여부


class Quiz:
    """개별 퀴즈 문항을 표현하는 클래스"""

    def __init__(self, question, choices, answer, points=DEFAULT_POINTS):
        """
        Quiz 객체 초기화 메서드
        :param question: 문제 내용 (str)
        :param choices: NUM_CHOICES개의 선택지 리스트 (list)
        :param answer: 정답 번호 1~NUM_CHOICES (int)
        :param points: 문항 배점 (int, 기본 1) - 옛 state.json에는 없어도 호환됨
        """
        self.question = question
        self.choices = choices
        self.answer = answer
        self.points = points

    def to_dict(self):
        """저장용 딕셔너리로 변환 (저장 구조가 바뀌면 이 메서드만 수정)"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "points": self.points,
        }

    def display(self):
        """퀴즈 문제와 선택지를 보기 좋게 콘솔에 출력하는 메서드"""
        print("\n----------------------------------------")
        print(f"{self.question}")
        for idx, choice in enumerate(self.choices, 1):
            print(f"  {idx}. {choice}")
        print("----------------------------------------")

    def check_answer(self, user_answer):
        """
        사용자가 입력한 답이 정답과 일치하는지 확인하는 메서드
        :param user_answer: 사용자가 입력한 정답 번호 (int)
        :return: 정답 여부 (bool)
        """
        return self.answer == user_answer


class QuizGame:
    """게임 전체의 흐름, 메뉴, 데이터 입출력을 관리하는 메인 컨트롤러 클래스"""

    def __init__(self, filename="state.json"):
        self.filename = filename
        self.backup_filename = filename + ".bak"
        self.data = self.load_data()
        self.quizzes = []
        self.load_quizzes_to_objects()

    # -----------------------------------------------------
    # 기본 데이터 / 검증
    # -----------------------------------------------------
    @staticmethod
    def default_data():
        """기본 퀴즈 5개와 최고 점수 0을 담은 초기 데이터를 반환"""
        return {
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

    @staticmethod
    def validate_data(data):
        """데이터 구조가 올바른지 검사. 문제가 있으면 ValueError 발생"""
        if not isinstance(data, dict):
            raise ValueError("최상위 데이터가 객체(dict)가 아닙니다.")
        if "quizzes" not in data or "best_score" not in data:
            raise ValueError("데이터 키값이 누락되었습니다.")
        if not isinstance(data["quizzes"], list):
            raise ValueError("quizzes 항목이 리스트가 아닙니다.")
        if not isinstance(data["best_score"], int):
            raise ValueError("best_score 항목이 정수가 아닙니다.")
        for i, q in enumerate(data["quizzes"], 1):
            if not isinstance(q, dict):
                raise ValueError(f"{i}번 퀴즈 형식이 올바르지 않습니다.")
            if not isinstance(q.get("question"), str) or not q["question"].strip():
                raise ValueError(f"{i}번 퀴즈의 문제 내용이 올바르지 않습니다.")
            choices = q.get("choices")
            if not isinstance(choices, list) or len(choices) != NUM_CHOICES:
                raise ValueError(f"{i}번 퀴즈의 선택지는 {NUM_CHOICES}개여야 합니다.")
            answer = q.get("answer")
            if not isinstance(answer, int) or not 1 <= answer <= NUM_CHOICES:
                raise ValueError(f"{i}번 퀴즈의 정답 번호가 올바르지 않습니다.")
        return True

    def _read_json_file(self, path):
        """JSON 파일을 읽고 구조까지 검증하여 반환 (실패 시 예외 발생)"""
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.validate_data(data)
        return data

    # -----------------------------------------------------
    # 불러오기 (복구 절차 포함)
    # -----------------------------------------------------
    def _try_restore_from_backup(self):
        """백업 파일(.bak)에서 복구를 시도. 성공하면 데이터, 실패하면 None"""
        if not os.path.exists(self.backup_filename):
            return None
        try:
            data = self._read_json_file(self.backup_filename)
            print(f"♻️ 백업 파일({self.backup_filename})에서 데이터를 복구했습니다.")
            return data
        except (OSError, json.JSONDecodeError, ValueError) as e:
            print(f"⚠️ 백업 파일도 사용할 수 없습니다. ({e})")
            return None

    def _quarantine_corrupted_file(self):
        """손상된 원본을 .corrupt 로 보관 (분석/수동 복구용). 실패해도 무시"""
        try:
            shutil.copy2(self.filename, self.filename + ".corrupt")
            print(f"🗂️ 손상된 원본을 {self.filename}.corrupt 로 보관했습니다.")
        except OSError:
            pass

    def load_data(self):
        """
        state.json 에서 퀴즈 데이터와 최고 점수를 불러오는 메서드
        복구 우선순위: ① state.json → ② state.json.bak → ③ 기본 데이터
        - 파일 없음 / JSON 손상 / 구조 오류 / 권한 오류를 각각 구분하여 처리
        """
        if not os.path.exists(self.filename):
            data = self._try_restore_from_backup()
            if data is None:
                print("📂 state.json 파일이 없어 기본 데이터로 생성합니다.")
                data = self.default_data()
            self.save_data(data)
            return data

        try:
            return self._read_json_file(self.filename)
        except PermissionError:
            print("🔒 state.json 읽기 권한이 없습니다. 파일 권한을 확인해주세요.")
            print("   (이번 실행은 저장 없이 임시 데이터로 진행합니다.)")
            return self._try_restore_from_backup() or self.default_data()
        except (json.JSONDecodeError, ValueError, UnicodeDecodeError) as e:
            print(f"⚠️ 경고: 데이터 파일이 손상되었습니다. 복구를 시도합니다. ({e})")
            self._quarantine_corrupted_file()
            data = self._try_restore_from_backup()
            if data is None:
                print("📂 백업이 없어 기본 데이터로 복구합니다.")
                data = self.default_data()
            self.save_data(data)
            return data
        except OSError as e:
            print(f"⚠️ 파일 읽기 오류 발생: {e}. 기본 데이터를 사용합니다.")
            return self.default_data()

    # -----------------------------------------------------
    # 저장 (자동 백업 + 원자적 쓰기)
    # -----------------------------------------------------
    def save_data(self, data=None):
        """
        현재 퀴즈 목록과 최고 점수를 state.json 에 저장하는 메서드
        1) 기존 정상 파일을 state.json.bak 로 백업
        2) 임시 파일(.tmp)에 먼저 쓰고 os.replace 로 교체 (쓰기 도중 중단돼도 원본 보호)
        :return: 저장 성공 여부 (bool)
        """
        if data is None:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.data.get("best_score", 0)
            }

        tmp_filename = self.filename + ".tmp"
        try:
            # 1) 현재 파일이 정상일 때만 백업 (손상본이 백업을 덮어쓰지 않도록)
            if os.path.exists(self.filename):
                try:
                    self._read_json_file(self.filename)
                    shutil.copy2(self.filename, self.backup_filename)
                except (OSError, json.JSONDecodeError, ValueError):
                    pass

            # 2) 임시 파일에 쓰고 교체
            with open(tmp_filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            os.replace(tmp_filename, self.filename)
            return True
        except PermissionError:
            print("🔒 데이터 저장 실패: 쓰기 권한이 없습니다. 폴더/파일 권한 또는 읽기 전용 속성을 확인하세요.")
        except OSError as e:
            print(f"⚠️ 데이터 저장 실패: {e}")
        # 실패 시 임시 파일 정리
        try:
            if os.path.exists(tmp_filename):
                os.remove(tmp_filename)
        except OSError:
            pass
        return False

    def load_quizzes_to_objects(self):
        """불러온 딕셔너리 데이터를 Quiz 인스턴스 리스트로 변환하는 메서드"""
        self.quizzes = [
            Quiz(
                q["question"],
                q["choices"],
                q["answer"],
                q.get("points", DEFAULT_POINTS),   # 옛 데이터(points 없음) 호환
            )
            for q in self.data.get("quizzes", [])
        ]

    @property
    def max_score(self):
        """모든 문항을 맞혔을 때의 만점(배점 합계)"""
        return sum(q.points for q in self.quizzes)

    # -----------------------------------------------------
    # 입력 / 메뉴
    # -----------------------------------------------------
    def get_validated_input(self, prompt, min_val, max_val):
        """
        공백 제거, 문자 입력(ValueError), 범위 초과, 빈 입력 및 안전 종료(Ctrl+C)를 처리하는 공통 입력 메서드
        """
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
        """콘솔 게임의 메인 실행 루프를 담당하는 메서드"""
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
        """
        등록된 모든 퀴즈를 출제하고 점수(배점 합계)를 계산하는 메서드
        - SHUFFLE_QUIZZES 가 True 이면 random.sample()로 문제 순서를 매번 랜덤하게 섞음
        - 원본 리스트(self.quizzes)는 그대로 두므로 목록 조회·저장 순서는 바뀌지 않음
        """
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요!")
            return

        # random.sample(): 원본을 건드리지 않고 섞인 새 리스트를 반환 (중복 없음)
        if SHUFFLE_QUIZZES:
            play_list = random.sample(self.quizzes, len(self.quizzes))
            print(f"\n📝 퀴즈를 시작합니다! (총 {len(play_list)}문제, 🔀 랜덤 순서)")
        else:
            play_list = self.quizzes
            print(f"\n📝 퀴즈를 시작합니다! (총 {len(play_list)}문제)")
        score = 0
        correct_count = 0

        for idx, q in enumerate(play_list, 1):
            print(f"\n[문제 {idx}/{len(play_list)}]")
            q.display()
            user_ans = self.get_validated_input(f"정답 입력 (1-{NUM_CHOICES}): ", 1, NUM_CHOICES)

            if q.check_answer(user_ans):
                print("✅ 정답입니다!")
                score += q.points
                correct_count += 1
            else:
                print(f"❌ 오답입니다! 정답은 {q.answer}번입니다.")

        print("\n========================================")
        print(f"🏆 결과: 총 {len(self.quizzes)}문제 중 {correct_count}문제 정답! ({score}/{self.max_score}점)")

        current_best = self.data.get("best_score", 0)
        if score > current_best:
            self.data["best_score"] = score
            self.save_data()
            print("🎉 새로운 최고 점수입니다!")
        print("========================================")

    def add_quiz(self):
        """새로운 퀴즈 문항을 입력받아 객체로 추가하고 파일에 저장하는 메서드"""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        try:
            question = input("문제를 입력하세요: ").strip()
            if not question:
                print("⚠️ 빈 문제는 추가할 수 없습니다.")
                return

            choices = []
            for i in range(1, NUM_CHOICES + 1):
                choice = input(f"선택지 {i}: ").strip()
                if not choice:
                    print("⚠️ 빈 선택지는 입력할 수 없습니다.")
                    return
                choices.append(choice)

            answer = self.get_validated_input(f"정답 번호 (1-{NUM_CHOICES}): ", 1, NUM_CHOICES)

            new_quiz = Quiz(question, choices, answer)
            self.quizzes.append(new_quiz)
            if self.save_data():
                print("✅ 퀴즈가 성공적으로 추가되어 저장되었습니다!")
            else:
                print("⚠️ 퀴즈는 이번 실행 중에만 유지되며 파일에는 저장되지 않았습니다.")
        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 입력을 취소합니다.")

    def show_quizzes(self):
        """
        현재 등록된 퀴즈 목록을 PAGE_SIZE 개씩 나누어 출력하는 메서드 (페이징)
        - Enter: 다음 페이지 / q: 목록 종료
        """
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        total = len(self.quizzes)
        print(f"\n📋 등록된 퀴즈 목록 (총 {total}개)")
        print("-" * 40)
        for start in range(0, total, PAGE_SIZE):
            for idx in range(start, min(start + PAGE_SIZE, total)):
                print(f"[{idx + 1}] {self.quizzes[idx].question}")
            print("-" * 40)
            if start + PAGE_SIZE >= total:
                break
            try:
                cmd = input(f"({start + PAGE_SIZE}/{total}) Enter: 다음 페이지, q: 종료 > ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                print()
                break
            if cmd == "q":
                break

    def show_score(self):
        """현재 저장된 최고 점수를 확인하는 메서드"""
        best = self.data.get("best_score", 0)
        print(f"\n🏆 최고 점수: {best}점")


if __name__ == "__main__":
    game = QuizGame()
    game.run()