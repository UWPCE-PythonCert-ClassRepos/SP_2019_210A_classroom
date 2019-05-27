# exceptions lab


def safe_input():
    def _input():
        return input('input something!\n')
    try:
        print(_input())
    except EOFError:
        print('end of file yo')
        return None
    except KeyboardInterrupt:
        print('input was cancelled\n')
        return None


safe_input()

