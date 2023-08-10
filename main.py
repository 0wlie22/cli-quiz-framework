"""
    This script is used to practice questions from the input file.
    It can be used in two modes:
        1. Normal mode: Practicing questions from start to end
        2. Practice mode: Practicing questions from wrong_questions.txt file
    Usage:
        python3 main.py -s 1 -e 10
        python3 main.py -b 1
        python3 main.py --practice
    Note:
        1. If you want to practice questions from a specific block, use -b option
        2. If you want to practice questions from a specific range, use -s and -e options
        3. If you want to practice questions from wrong_questions.txt file, use --practice option
"""

import argparse
import os
import re

from colorama import Fore, Style

INPUT_FILE = "input.txt"
WRONG_QUESTIONS_FILE = "wrong_questions.txt"


def print_colored(text, color=Fore.WHITE) -> None:
    """
    Print text in color

    Args:
        text (str): Text to print
        color (str, optional): Color to print text in. Defaults to Fore.WHITE.
    """
    print(f"{color}{text}{Style.RESET_ALL}")


def parse_line(line: str) -> str:
    """
    Parse line to determine if it is a question or an answer

    Args:
        line (str): Line to parse

    Returns:
        str: "question" if line is a question, "answer" if line is an answer, "" otherwise

    """

    # if line contains arabic number
    if re.search(r"^[0-9]*\.", line):
        return "question"
    # if line starts with a, b, c, d
    if re.search(r"^[a-d]\.", line):
        return "answer"

    return ""


def get_answer(question_number: int) -> str:
    """

    Args:
        question_number (int): Question number

    Returns:
        str: Correct answer for the question

    """
    with open("answers.txt", "r", encoding="utf-8") as file:
        answers = file.readline()
        return answers[question_number - 1]


def ask_question(question, answers, correct_answer) -> bool:
    """
    Ask question and check if answer is correct

    Args:
        question (str): Question to ask
        answers (list): List of answers
        correct_answer (str): Correct answer

    Returns:
        bool: True if answer is correct, False otherwise
    """
    os.system("clear")
    print_colored("\n" + question.strip(), Fore.CYAN)
    for _, answer in enumerate(answers):
        print_colored(answer.strip())
    user_answer = input(f"{Fore.YELLOW}Enter your answer: {Style.RESET_ALL}")
    while user_answer not in ["a", "b", "c", "d"]:
        user_answer = input(
            f"{Fore.RED}Wrong answer!\n{Fore.YELLOW}Enter your answer: {Style.RESET_ALL}"
        )
    if user_answer == correct_answer:
        print_colored("Correct!", Fore.GREEN)
        os.system("sleep 1")
        return True
    print_colored(f"Wrong! Correct answer is {correct_answer}", Fore.RED)
    os.system("sleep 1")
    return False


def write_wrong_questions(wrong_questions) -> None:
    """
    Write wrong questions to wrong_questions.txt file

    Args:
        wrong_questions (list): List of wrong questions

    """
    with open(WRONG_QUESTIONS_FILE, "a", encoding="utf-8") as file:
        for question in wrong_questions:
            file.write(str(question) + "\n")


def practice_mode() -> None:
    """
    Practice questions from wrong_questions.txt file
    """
    questions = []
    with open(WRONG_QUESTIONS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            try:
                questions.append(int(line.strip()))
            except ValueError:
                # if line is empty
                pass

    questions = list(dict.fromkeys(sorted(questions)))

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line_type = parse_line(line)
            if not line_type:
                continue

            if line_type == "question":
                question_number = int(line.split(".")[0])
                if question_number in questions:
                    result = ask_question(
                        line,
                        [next(file) for _ in range(5)],
                        get_answer(question_number),
                    )
                    if result:
                        questions.remove(question_number)
                        if not questions:
                            print_colored(
                                "You answered all questions correctly!", Fore.GREEN
                            )
                            return


def normal_mode(start_question, end_qustion) -> None:
    """
    Practice questions from start_question to end_question

    Args:
        start_question (int): Start question number
        end_qustion (int): End question number
    """
    print_flag = False
    question_count = 0
    question_number = 0
    wrong_questions = []

    with open(INPUT_FILE, "r", encoding="latin-1") as file:
        for line in file:
            line_type = parse_line(line)
            if not line_type:
                continue

            if line_type == "question":
                question_number = int(line.split(".")[0])

            if question_number == start_question:
                print_flag = True
            if question_number == end_qustion + 1:
                questions_total = end_qustion - start_question + 1
                print_colored(
                    f"\nYou answered {question_count}/{questions_total}", Fore.CYAN
                )
                write_wrong_questions(wrong_questions)
                print_flag = False
                return

            if print_flag:
                result = ask_question(
                    line, [next(file) for _ in range(5)], get_answer(question_number)
                )
                if result:
                    question_count += 1
                else:
                    wrong_questions.append(int(line.split(".")[0]))


def main(args):
    """
    Main function
    """
    if args.b >= 0:
        args.s = args.b * 10
        args.e = args.b * 10 + 9

    if args.practice:
        practice_mode()
    else:
        normal_mode(args.s, args.e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", type=int, default=1, help="Start question number")
    parser.add_argument("-e", type=int, default=285, help="End question number")
    parser.add_argument("-b", type=int, default=-1, help="Block number")
    parser.add_argument("--practice", action="store_true", help="Practice mode")
    arguments = parser.parse_args()

    try:
        main(arguments)
    except KeyboardInterrupt:
        print_colored("\nExiting without saving...", Fore.RED)
