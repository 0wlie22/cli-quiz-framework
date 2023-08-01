import re
import argparse

from colorama import Fore, Style

def print_colored(text, color=Fore.WHITE):
    print(f"{color}{text}{Style.RESET_ALL}")


def parse_line(line: str) -> str:
    # if line contains arabic number
    if re.search(r"^[0-9]*\.", line):
        return "question"
    # if line starts with a, b, c, d
    if re.search(r"^[a-d]\.", line):
        return "answer"

    return ""


def get_answer(question_number: int) -> str:
    with open("answers.txt", "r") as f:
        answers = f.readline()
        return answers[question_number - 1]


def ask_question(question, answers, correct_answer):
    print_colored(question, Fore.YELLOW)
    for _, answer in enumerate(answers):
        print_colored(answer)
    user_answer = input("Enter your answer: ")
    if user_answer == correct_answer:
        print_colored("Correct!", Fore.GREEN)
    else:
        print_colored(f"Wrong! Correct answer is {correct_answer}", Fore.RED)
    

def main(start_question, end_qustion):
    print_flag = False
    with open("input.txt", "r") as f:
        for line in f:
            line_type = parse_line(line)
            if not line_type:
                continue

            if line_type == "question" and int(line.split(".")[0]) == start_question:
                print_flag = True
            if line_type == "question" and int(line.split(".")[0]) == end_qustion + 1:
                print_flag = False
                return

            if print_flag:
                ask_question(line, [next(f) for _ in range(5)],
                             get_answer(int(line.split(".")[0])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", type=int, default=1, help="start question number")
    parser.add_argument("-e", type=int, default=285, help="end question number")
    args = parser.parse_args()
    try:
        main(args.s, args.e)
    except KeyboardInterrupt:
        print("\nExiting...")

