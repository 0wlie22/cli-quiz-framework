"""
    This scrwrite_wrong_questions(wrong_questions)
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
    if args.b == 0:
        args.s += 1

    if args.practice:
        practice_mode()
    else:
        normal_mode(args.s, args.e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", type=int, default=1, help="Start question number")
    parser.add_argument("-e", type=int, default=286, help="End question number")
    parser.add_argument("-b", type=int, default=-1, help="Block number")
    parser.add_argument("--practice", action="store_true", help="Practice mode")
    arguments = parser.parse_args()

    try:
        main(arguments)
    except KeyboardInterrupt:
        print_colored("\nExiting without saving...", Fore.RED)
