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


def ask_question(question, answers, correct_answer) -> bool:
    print_colored("\n" + question.strip(), Fore.CYAN)
    for _, answer in enumerate(answers):
        print_colored(answer.strip())
    user_answer = input(f"{Fore.YELLOW}Enter your answer: {Style.RESET_ALL}")
    if user_answer == correct_answer:
        print_colored("Correct!", Fore.GREEN)
        return True
    else:
        print_colored(f"Wrong! Correct answer is {correct_answer}", Fore.RED)
        return False
    

def main(start_question, end_qustion, block=-1):
    if block >= 0:
        start_question = block * 10
        end_qustion = block * 10 + 9
    print_flag = False
    question_count = 0
    with open("input.txt", "r") as f:
        for line in f:
            line_type = parse_line(line)
            if not line_type:
                continue

            if line_type == "question" and int(line.split(".")[0]) == start_question:
                print_flag = True
            if line_type == "question" and int(line.split(".")[0]) == end_qustion + 1:
                questions_total = end_qustion - start_question + 1
                print_colored(f"\nYou answered {question_count}/{questions_total}", Fore.CYAN)
                print_flag = False
                return

            if print_flag:
                result = ask_question(line, [next(f) for _ in range(5)], get_answer(int(line.split(".")[0])))
                if result:
                    question_count += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", type=int, default=1, help="start question number")
    parser.add_argument("-e", type=int, default=285, help="end question number")
    parser.add_argument("-b", type=int, help="block number")
    args = parser.parse_args()
    try:
        main(args.s, args.e, args.b)
    except KeyboardInterrupt:
        print_colored("\nExiting...", Fore.RED)

