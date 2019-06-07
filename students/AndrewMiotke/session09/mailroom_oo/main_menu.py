from main_menu import mailroom

def main_menu():
    while True:
        answer = input(""" -> What you would you like to do?
    Pick One:
    1: Send a thank you
    2: Create a report
    3: Send letters to ALL donors
    4: Quit
    >>> """)
        print(f"You selected {answer}")

        answer = answer.strip()

        try:
            answer_dict = {
                "1": mailroom.send_thank_you_letter,
                "2": mailroom.report,
                "3": mailroom.send_letter_to_all_donors,
                "4": mailroom.quit_mailroom,
            }

            answer_dict.get(answer)()
        except TypeError:
            print(f"\n‼️  ️{answer} is not a valid option, please select from 1, 2, 3 or 4\n")


if __name__ == "__main__":
    main_menu()