import contextlib
try:
    import msvcrt
    WINDOWS = True
except ImportError:
    import sys
    import tty
    import termios
    WINDOWS = False

from pprint import pprint

from .keycodes import KeyCodes, RawInput


def _build_tree(key):
    tree = {}
    for value in KeyCodes.__dict__.values():
        code = list(reversed(getattr(value, key, '')))
        if not code:
            continue

        node = tree
        while True:
            c = code.pop()
            if code:
                node = node.setdefault(c, {})
            else:
                if c in node:
                    raise ValueError('duplicate keycodes {} {}'.format(value, node[c]))
                node[c] = value
                break
    return tree


def get_char_wrap(get_char):
    def inner():
        char = get_char(1)
        if char not in _tree:
            return RawInput(char)

        node = _tree[char]
        while isinstance(node, dict):
            node = node[get_char(1)]
        return node
    return inner


if WINDOWS:
    _tree = _build_tree('_windows')


    def _getch(number):
        return ''.join(msvcrt.getwch() for _ in range(number))


    @contextlib.contextmanager
    def raw_prompt():
        try:
            yield get_char_wrap(_getch)
        finally:
            pass
else:
    _tree = _build_tree('_unix')

    @contextlib.contextmanager
    def raw_prompt():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            yield get_char_wrap(sys.stdin.read)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
