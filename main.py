import re
import colorama

from colorama import Fore, Style

def read_answer_for_topic(topic_number, all_answers):
    return all_answers[topic_number - 1]

def parse_input_file(input_file):
    with open(input_file, 'r', encoding='latin-1') as file:
        content = file.read()

    question_pattern = r'(?m)^(\d+\. .+)$'
    answer_pattern = r'(?m)^[a-d]\. .+$'
    questions = []

    current_question_text = None
    current_answers = []

    for line in content.splitlines():
        question_match = re.match(question_pattern, line)
        answer_match = re.match(answer_pattern, line)

        if question_match:
            if current_question_text and current_answers:
                questions.append({
                    'question': current_question_text,
                    'answers': current_answers
                })
            current_question_text = question_match.group(1)
            current_answers = []
        elif answer_match:
            current_answers.append(answer_match.group(0)[3:])

    if current_question_text and current_answers:
        questions.append({
            'question': current_question_text,
            'answers': current_answers
        })

    return questions

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def ask_question(topic_number, questions, all_answers):
    print_colored(f"Topic {topic_number}:", Fore.WHITE)
    questions_answered = 0
    question_number = 0
    for question_data in questions:
        question_text = question_data['question']
        answers = question_data['answers']

        # Print question and answers
        print_colored("\n" + question_text, Fore.CYAN)
        for i, answer in enumerate(answers, start=1):
            print_colored(f"{chr(96 + i)}. {answer}", Fore.WHITE)

        user_answer = input(f"{Fore.YELLOW}Your answer: {Style.RESET_ALL}")
        user_answer_index = ord(user_answer) - 96

        correct_answer = (read_answer_for_topic(topic_number, all_answers))[question_number]

        if user_answer_index == ord(correct_answer) - 96:
            questions_answered += 1
            print_colored("Correct!", Fore.GREEN)
        else:
            print_colored(f"Wrong! The correct answer is {correct_answer}.", Fore.RED)
        question_number += 1

    print_colored(f"\nYou answered {questions_answered} out of {len(questions)} questions correctly.", Fore.YELLOW)

def main():
    colorama.init(autoreset=True)
    
    answers = []
    with open("answers", 'r', encoding='utf-8') as file:
        for line in file:
            answers.append(line.strip())

    while True:
        try:
            topic_number = int(input("Enter a topic number (1 to 10) or 0 to exit: "))
            if topic_number == 0:
                break
            elif 1 <= topic_number <= 10:
                input_file = f"input{topic_number}"
                questions = parse_input_file(input_file)
                ask_question(topic_number, questions, answers)
            else:
                print_colored("Invalid topic number. Please enter a number between 1 and 10.", Fore.RED)
        except ValueError:
            print_colored("Invalid input. Please enter a valid topic number (1 to 10) or 0 to exit.", Fore.RED)

if __name__ == "__main__":
    main()

