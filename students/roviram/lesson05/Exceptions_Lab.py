#-----------------------------------------------------------------#
# Dev: Miguel Rovira-Gonzalez
# Changelog: Miguel Rovira-Gonzalez, Created Script, May 11th, 2019
#------------------------------------------------------------------#
from textwrap import dedent

def safe_input():
    try:
        user_input = input("Hey, what are you favorite things to do outside of work? ")
        return user_input

    except (EOFError, KeyboardInterrupt):
        return None


def main_body():
    user_data = safe_input()
    if user_data is None:
        print("""\nThere is something wrong with the users data, the user either entered (ctrl + c), (ctrl + d) or (ctrl + z). """)
    else:
        print(user_data)


if __name__ == '__main__':
    main_body()
