#!/usr/bin/env python3

def safe_input():
    try:
        prompt = input('Please type something')
        print(prompt)
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None

if __name__ == '__main__':
    safe_input()
