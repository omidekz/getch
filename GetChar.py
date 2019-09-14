from sys import stdout

ENTER_ORD = 13
BACKSPACE_ORD = 127


class _GetWindows:
    def __init__(self):
        import msvcrt

    def __call__(self, *args, **kwargs):
        import msvcrt
        return msvcrt.getch()


class _Unix:
    def __init__(self):
        import tty, sys, termios

    def __call__(self, *args, **kwargs):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetCh:
    def __init__(self):
        try:
            self.impl = _GetWindows()
        except ImportError:
            self.impl = _Unix()

    def __call__(self, *args, **kwargs):
        return self.impl()

    def getch(self):
        return self()


def getch(message=None, clear_line_after_getch=False):
    if not message:
        return _GetCh()()
    print_in_line(message)
    ch = _GetCh()()
    if clear_line_after_getch:
        print('\r', end='')
        for i in range(len(message)):
            print(' ', end='')
        print('\r', end='')
    return ch


def password(message, replace_with='*') -> list:
    print_in_line(message)
    passwd = []
    while True:
        ch = getch()
        if ord(ch) == ENTER_ORD:
            print()
            return passwd
        if ord(ch) == BACKSPACE_ORD:
            if len(passwd) > 0:
                print_in_line('\b \b')
                passwd.pop()
            else:
                print_in_line('\a')
        else:
            print_in_line(replace_with)
            passwd.append(ch)


def pause(message='Press any key...', return_key=False):
    ch = getch(message, True)
    if return_key:
        return ch


def print_in_line(message):
    print(message, end='')
    stdout.flush()
