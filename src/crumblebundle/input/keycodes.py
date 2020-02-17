class _KeyCode:
    __slots__ = ('_windows', '_unix')
    raw = False

    def __init__(self, windows, unix):
        self._windows = windows
        self._unix = unix

    def __repr__(self):
        return '_KeyCode(windows={self._windows!r}, unix={self._unix!r})'.format(self=self)


class KeyCodes:
    BACKSPACE =     _KeyCode(windows='\x08',     unix='')
    TAB =           _KeyCode(windows='\t',       unix='')
    ENTER =         _KeyCode(windows='\r',       unix='')
    ESCAPE =        _KeyCode(windows='\x1b',     unix='')
    SPACE =         _KeyCode(windows=' ',        unix='')
    PAGE_UP =       _KeyCode(windows='\xe0I',    unix='')
    PAGE_DOWN =     _KeyCode(windows='\xe0Q',    unix='')
    END =           _KeyCode(windows='\xe0O',    unix='')
    HOME =          _KeyCode(windows='\xe0G',    unix='')
    LEFT_ARROW =    _KeyCode(windows='\xe0K',    unix='')
    UP_ARROW =      _KeyCode(windows='\xe0H',    unix='')
    RIGHT_ARROW =   _KeyCode(windows='\xe0M',    unix='')
    DOWN_ARROW =    _KeyCode(windows='\xe0P',    unix='')
    INSERT =        _KeyCode(windows='\xe0R',    unix='')
    DELETE =        _KeyCode(windows='\xe0S',    unix='')
    F1 =            _KeyCode(windows='\x00;',    unix='')
    F2 =            _KeyCode(windows='\x00<',    unix='')
    F3 =            _KeyCode(windows='\x00=',    unix='')
    F4 =            _KeyCode(windows='\x00>',    unix='')
    F5 =            _KeyCode(windows='\x00?',    unix='')
    F6 =            _KeyCode(windows='\x00@',    unix='')
    F7 =            _KeyCode(windows='\x00A',    unix='')
    F8 =            _KeyCode(windows='\x00B',    unix='')
    F9 =            _KeyCode(windows='\x00C',    unix='')
    F10 =           _KeyCode(windows='\x00D',    unix='')
    F11 =           _KeyCode(windows='\xe0\x85', unix='')
    F12 =           _KeyCode(windows='\xe0\x86', unix='')
    KEYPAD_0 =      _KeyCode(windows='\x00R',    unix='')
    KEYPAD_1 =      _KeyCode(windows='\x00O',    unix='')
    KEYPAD_2 =      _KeyCode(windows='\x00P',    unix='')
    KEYPAD_3 =      _KeyCode(windows='\x00Q',    unix='')
    KEYPAD_4 =      _KeyCode(windows='\x00K',    unix='')
    # KEYPAD_5 =      _KeyCode(windows='\x00',    unix='')
    KEYPAD_6 =      _KeyCode(windows='\x00M',    unix='')
    KEYPAD_7 =      _KeyCode(windows='\x00G',    unix='')
    KEYPAD_8 =      _KeyCode(windows='\x00H',    unix='')
    KEYPAD_9 =      _KeyCode(windows='\x00I',    unix='')
    KEYPAD_DOT =    _KeyCode(windows='\x00S',    unix='')
    INTERRUPT =     _KeyCode(windows='\x03',     unix='')


class RawInput:
    __slots__ = ('value',)
    raw = True

    def __init__(self, value):
        self.value = value
