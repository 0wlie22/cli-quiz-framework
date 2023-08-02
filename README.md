# CLI Quiz Maker

The CLI Quiz Maker is a Python command-line tool that allows you to take a quiz by reading questions and answers from the provided input files. You can specify the range of questions to be included in the quiz or take a specific block of questions.

## Requirements

Python 3.x

`pip install -r requirements.txt`

## Usage

`python main.py [-h] [-s START_QUESTION] [-e END_QUESTION] [-b BLOCK_NUMBER]`

## Arguments

-s START_QUESTION: The number of the first question in the quiz. The default is 1.

-e END_QUESTION: The number of the last question in the quiz. The default is 285.

-b BLOCK_NUMBER: If specified, only questions within the specified block will be included in the quiz. Each block contains 10 questions (e.g., -b 0 will include questions 1 to 10, -b 1 will include questions 11 to 20, and so on).

--practice PRACTICE_MODE: If passed, only the questions answered wrong in the normal mode would be
showed

## Input Files

The quiz questions, answers, and correct answers are read from two input files:

**input.txt**: Contains the questions and their corresponding answer choices.
Questions are marked by lines starting with an Arabic number followed by a period (e.g., "1.", "2.", etc.).
Answer choices are marked by lines starting with a lowercase letter followed by a period (e.g., "a.", "b.", "c.", "d.", etc.).

**answers.txt**: Contains the correct answers for each question, all answers in one line. The nth character in this file corresponds to the correct answer for the nth question.

## Quiz Taking

* **Normal mode**: the CLI Quiz Maker will present the questions one by one and prompt you to choose an answer by typing the letter of your choice (a, b, c, or d). After you enter your answer, the program will inform you if your answer is correct or incorrect. At the end of the quiz, it will display the number of questions you answered correctly out of the total questions in the quiz.
* **Practice mode**: all the questions answered wrong in the normal mode, would be revised and presented one more time

## Examples

```python
# Take the full quiz from question 1 to question 285:
python main.py

# Take the quiz from question 50 to question 70:
python main.py -s 50 -e 70

# Take the quiz for block 3 (questions 21 to 30):
python main.py -b 2

# Revise all the wo=rong questions
python main.py --practice
```

## Exiting

To exit the quiz at any point during the quiz-taking process, press Ctrl+C.

**WARNING**: with exiting wrong questions won't be saved.

