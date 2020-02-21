import enum

import colorama

from .helpers import Dict
from .input import KeyCodes, raw_prompt

colorama.init()


class Cursor(enum.IntFlag):
    NONE = 0
    SELECTED = enum.auto()
    HOVER = enum.auto()


USAGE = object()
clean = "\x1b[{}A\x1b[J".format
PROMPT = "{fg.GREEN}?{fg.RESET} {st.BRIGHT}{fg.YELLOW}{{}}:{st.RESET_ALL} {fg.CYAN}{{}}{st.RESET_ALL}".format(
    fg=colorama.Fore, st=colorama.Style
)
DEFAULT = "{fg.BLACK}{st.BRIGHT}{{}}{st.RESET_ALL}".format(
    fg=colorama.Fore, st=colorama.Style
)
OPTION = {
    USAGE: "{fg.RESET}(Use arrow keys){fg.RESET}".format(fg=colorama.Fore),
    Cursor.NONE: "{fg.RESET}> {{}}{fg.RESET}".format(fg=colorama.Fore),
    Cursor.HOVER: "{fg.BLUE}> {{}}{fg.RESET}".format(fg=colorama.Fore),
}
MULTI = {
    USAGE: "{fg.RESET}(Press {fg.CYAN}{st.BRIGHT}<space>{st.RESET_ALL}{fg.RESET} to select, {fg.CYAN}{st.BRIGHT}<a>{st.RESET_ALL}{fg.RESET} to toggle all, {fg.CYAN}{st.BRIGHT}<i>{st.RESET_ALL}{fg.RESET} to invert selection){st.RESET_ALL}".format(
        fg=colorama.Fore, st=colorama.Style
    ),
    Cursor.NONE: "{fg.RESET} ( ) {{}}{fg.RESET}".format(fg=colorama.Fore),
    Cursor.HOVER: "{fg.CYAN}>( ) {{}}{fg.RESET}".format(fg=colorama.Fore),
    Cursor.SELECTED: " {fg.GREEN}(*){fg.RESET} {{}}{fg.RESET}".format(fg=colorama.Fore),
    Cursor.SELECTED
    | Cursor.HOVER: "{fg.CYAN}>{fg.GREEN}(*){fg.CYAN} {{}}{fg.RESET}".format(
        fg=colorama.Fore
    ),
}


class Value:
    def __init__(self, orig, map, flags):
        self.orig = orig
        self._map = map

        self._fmt = ""
        self._flags = None
        self.flags = flags

    @property
    def flags(self):
        return self._flags

    @flags.setter
    def flags(self, flags):
        if flags != self._flags:
            self._flags = flags
            self._fmt = self._map[flags].format(self.orig)

    def __str__(self):
        return self._fmt


class Input:
    def __init__(self, instance):
        self.instance = instance

    def value(self, prompt, output, default):
        default = Dict.get(self.instance.dependency.config, output, default)
        default = self.instance.dependency.env.from_string(default).render(
            cookiecutter=self.instance.cookiecutter
        )
        value = []
        from_end = 0
        with raw_prompt() as get_char:
            while True:
                print(
                    "\r\x1b[K"
                    + PROMPT.format(prompt, "".join(value) or DEFAULT.format(default)),
                    end="\b" * (from_end if value else len(default)),
                )
                char = get_char()
                if char.raw:
                    value.insert(len(value) - from_end, char.value)
                else:
                    if char is KeyCodes.ENTER:
                        print()
                        return "".join(value) or default
                    elif char is KeyCodes.BACKSPACE:
                        if from_end < len(value):
                            value.pop(len(value) - from_end - 1)
                    elif char is KeyCodes.DELETE:
                        if from_end:
                            value.pop(len(value) - from_end)
                        from_end = max(from_end - 1, 0)
                    elif char is KeyCodes.RIGHT_ARROW:
                        from_end = max(from_end - 1, 0)
                    elif char is KeyCodes.LEFT_ARROW:
                        from_end = min(from_end + 1, len(value))
                    elif char is KeyCodes.HOME:
                        from_end = len(value)
                    elif char is KeyCodes.END:
                        from_end = 0
                    elif char is KeyCodes.INTERRUPT:
                        raise KeyboardInterrupt()

    def option(self, prompt, output, options, default):
        default = Dict.get(self.instance.dependency.config, output, default)
        if isinstance(default, str):
            default = self.instance.dependency.env.from_string(default).render(
                cookiecutter=self.instance.cookiecutter
            )
        else:
            raise ValueError("choice default was not an expected type")
        try:
            index = options.index(default)
        except ValueError:
            raise ValueError("default is not an available option") from None

        c_options = [Value(o, OPTION, Cursor.NONE) for o in options]
        c_options[index].flags = Cursor.HOVER
        with raw_prompt() as get_char:
            print("{}:".format(prompt))
            print("\n" * len(c_options), end="")
            while True:
                print(clean(len(c_options)) + "\n".join(map(str, c_options)))
                char = get_char()
                if char.raw:
                    continue

                if char is KeyCodes.ENTER:
                    print(
                        clean(len(c_options) + 1)
                        + PROMPT.format(prompt, c_options[index].orig)
                    )
                    return c_options[index].orig

                if char is KeyCodes.UP_ARROW or char is KeyCodes.DOWN_ARROW:
                    old_index = index
                    index = (index + (-1 if char == KeyCodes.UP_ARROW else 1)) % len(
                        options
                    )
                    c_options[old_index].flags &= ~Cursor.HOVER
                    c_options[index].flags |= Cursor.HOVER
                elif char is KeyCodes.INTERRUPT:
                    raise KeyboardInterrupt()

    def multiple(self, prompt, output, options, default):
        default = Dict.get(self.instance.dependency.config, output, default)
        if isinstance(default, str):
            default = self.instance.dependency.env.from_string(default).render(
                cookiecutter=self.instance.cookiecutter
            )
        else:
            raise ValueError("multiple default was not an expected type")
        try:
            index = options.index(default)
        except ValueError:
            raise ValueError("default is not an available option") from None

        c_options = [Value(o, MULTI, Cursor.NONE) for o in options]
        c_options[index].flags = Cursor.HOVER
        with raw_prompt() as get_char:
            description = MULTI[USAGE]
            print(PROMPT.format(prompt, description))
            print("\n" * len(c_options), end="")
            while True:
                print(clean(len(c_options)) + "\n".join(map(str, c_options)))
                char = get_char()
                if char.raw:
                    if char.value == "a":
                        for option in c_options:
                            option.flags |= Cursor.SELECTED
                    elif char.value == "i":
                        for option in c_options:
                            option.flags ^= Cursor.SELECTED
                if char is KeyCodes.SPACE:
                    c_options[index].flags |= Cursor.SELECTED
                if char is KeyCodes.ENTER:
                    values = tuple(
                        o.orig for o in c_options if o.flags & Cursor.SELECTED
                    )
                    print(
                        clean(len(c_options) + 1)
                        + PROMPT.format(prompt, ", ".join(values))
                    )
                    return values
                elif char is KeyCodes.UP_ARROW or char is KeyCodes.DOWN_ARROW:
                    old_index = index
                    index = (index + (-1 if char == KeyCodes.UP_ARROW else 1)) % len(
                        options
                    )
                    c_options[old_index].flags &= ~Cursor.HOVER
                    c_options[index].flags |= Cursor.HOVER
                elif char is KeyCodes.INTERRUPT:
                    raise KeyboardInterrupt()


class ReqInput:
    def __init__(self, requirements, config, env):
        self.requirements = requirements
        self.config = config
        self.env = env

    def value(self, prompt, output, default):
        default = Dict.get(self.config, output, default)
        ret = self.env.from_string(default).render(cookiecutter=self.requirements)
        return ret

    def option(self, prompt, output, options, default):
        default = Dict.get(self.config, output, default)
        ret = self.env.from_string(default).render(cookiecutter=self.requirements)
        return ret

    def multiple(self, prompt, output, options, default):
        default = Dict.get(self.config, output, default)
        ret = self.env.from_string(default).render(cookiecutter=self.requirements)
        return ret
