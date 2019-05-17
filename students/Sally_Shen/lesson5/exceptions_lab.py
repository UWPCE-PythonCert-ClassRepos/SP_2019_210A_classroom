

def safe_input():
    try:
        a_input = input('Please give some input:')
    except (EOFError, KeyboardInterrupt):
        return None
    return a_input


print(safe_input())

