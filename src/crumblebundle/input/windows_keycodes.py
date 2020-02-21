# Table headers
# [name,       ext, ext-shift, ext-ctrl,  ext-alt]
# [name, dec, char, dec, char, dec char, dec char]
_keycodes = [
    ["ESC", 1, 27, None, 27, None, 27, None, 1, 0],
    ["1!", 2, 49, "1", 33, "!", None, None, 120, 0],
    ["2@", 3, 50, "2", 64, "@", 3, 0, 121, 0],
    ["3#", 4, 51, "3", 35, "#", None, None, 122, 0],
    ["4$", 5, 52, "4", 36, "$", None, None, 123, 0],
    ["5%", 6, 53, "5", 37, "%", None, None, 124, 0],
    ["6^", 7, 54, "6", 94, "^", 30, "\x1e", 125, 0],
    ["7&", 8, 55, "7", 38, "&", None, None, 126, 0],
    ["8*", 9, 56, "8", 42, "*", None, None, 127, 0],
    ["9(", 10, 57, "9", 40, "(", None, None, 128, 0],
    ["0)", 11, 48, "0", 41, ")", None, None, 129, 0],
    ["-_", 12, 45, "-", 95, "_", 31, "\x1f", 130, 0],
    ["=+", 13, 61, "=", 43, "+", None, None, 131, 0],
    ["BKSP", 14, 8, None, 8, None, 127, None, 14, 0],
    ["TAB", 15, 9, None, 15, 0, 148, 0, 15, 0],
    ["Q", 16, 113, "q", 81, "Q", 17, "\x11", 16, 0],
    ["W", 17, 119, "w", 87, "W", 23, "\x17", 17, 0],
    ["E", 18, 101, "e", 69, "E", 5, "\x05", 18, 0],
    ["R", 19, 114, "r", 82, "R", 18, "\x12", 19, 0],
    ["T", 20, 116, "t", 84, "T", 20, "SO", 20, 0],
    ["Y", 21, 121, "y", 89, "Y", 25, "\x19", 21, 0],
    ["U", 22, 117, "u", 85, "U", 21, "\x15", 22, 0],
    ["I", 23, 105, "i", 73, "I", 9, "\t", 23, 0],
    ["O", 24, 111, "o", 79, "O", 15, "\x0f", 24, 0],
    ["P", 25, 112, "p", 80, "P", 16, "\x10", 25, 0],
    ["[{", 26, 91, "[", 123, "{", 27, "\x1b", 26, 0],
    ["]}", 27, 93, "]", 125, "}", 29, "\x1d", 27, 0],
    ["ENTER", 28, 13, "\r", 13, "\r", 10, "\x0a", 28, 0],
    ["ENTER£", 28, 13, "\r", 13, "\r", 10, "\x0a", 166, 0],
    ["LCTRL", 29, None, None, None, None, None, None, None, None],
    ["RCTRL£", 29, None, None, None, None, None, None, None, None],
    ["A", 30, 97, "a", 65, "A", 1, "\x01", 30, 0],
    ["S", 31, 115, "s", 83, "S", 19, "\x13", 31, 0],
    ["D", 32, 100, "d", 68, "D", 4, "\x04", 32, 0],
    ["F", 33, 102, "f", 70, "F", 6, "\x06", 33, 0],
    ["G", 34, 103, "g", 71, "G", 7, "\a", 34, 0],
    ["H", 35, 104, "h", 72, "H", 8, "\b", 35, 0],
    ["J", 36, 106, "j", 74, "J", 10, "\x0a", 36, 0],
    ["K", 37, 107, "k", 75, "K", 11, "\v", 37, 0],
    ["L", 38, 108, "l", 76, "L", 12, "\f", 38, 0],
    [";:", 39, 59, ";", 58, ":", None, None, 39, 0],
    ["'\"", 40, 39, "'", 34, '"', None, None, 40, 0],
    ["`~", 41, 96, "`", 126, "~", None, None, 41, 0],
    ["L SHIFT", 42, None, None, None, None, None, None, None, None],
    ["\\|", 43, 92, "\\", 124, "|", 28, "\x1c", None, None],
    ["Z", 44, 122, "z", 90, "Z", 26, "\x1a", 44, 0],
    ["X", 45, 120, "x", 88, "X", 24, "\x18", 45, 0],
    ["C", 46, 99, "c", 67, "C", 3, "\x03", 46, 0],
    ["V", 47, 118, "v", 86, "V", 22, "\x16", 47, 0],
    ["B", 48, 98, "b", 66, "B", 2, "\x02", 48, 0],
    ["N", 49, 110, "n", 78, "N", 14, "\x0e", 49, 0],
    ["M", 50, 109, "m", 77, "M", 13, "\x0d", 50, 0],
    [",<", 51, 44, ",", 60, "<", None, None, 51, 0],
    [".>", 52, 46, ".", 62, ">", None, None, 52, 0],
    ["/?", 53, 47, "/", 63, "?", None, None, 53, 0],
    ["GRAY/£", 53, 47, "/", 63, "?", 149, 0, 164, 0],
    ["R SHIFT", 54, None, None, None, None, None, None, None, None],
    ["PRISC", 55, 42, "*", "PRISC", "✝✝", 16, None, None, None],
    ["L ALT", 56, None, None, None, None, None, None, None, None],
    ["R ALT£", 57, None, None, None, None, None, None, None, None],
    ["SPACE", 57, 32, " ", 32, " ", 32, " ", 32, " "],
    ["CAPS", 58, None, None, None, None, None, None, None, None],
    ["F1", 59, 59, 0, 84, 0, 94, 0, 104, 0],
    ["F2", 60, 60, 0, 85, 0, 95, 0, 105, 0],
    ["F3", 61, 61, 0, 86, 0, 96, 0, 106, 0],
    ["F4", 62, 62, 0, 87, 0, 97, 0, 107, 0],
    ["F5", 63, 63, 0, 88, 0, 98, 0, 108, 0],
    ["F6", 64, 64, 0, 89, 0, 99, 0, 109, 0],
    ["F7", 65, 65, 0, 90, 0, 100, 0, 110, 0],
    ["F8", 66, 66, 0, 91, 0, 101, 0, 111, 0],
    ["F9", 67, 67, 0, 92, 0, 102, 0, 112, 0],
    ["F10", 68, 68, 0, 93, 0, 103, 0, 113, 0],
    ["F11£", 87, 133, 0xE0, 135, 0xE0, 137, 0xE0, 139, 0xE0],
    ["F12£", 88, 134, 0xE0, 136, 0xE0, 138, 0xE0, 140, 0xE0],
    ["NUM", 69, None, None, None, None, None, None, None, None],
    ["HOME", 71, 71, 0, 55, "7", 119, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["HOME£", 71, 71, 0xE0, 71, 0xE0, 119, 0xE0, 151, 0],
    ["UP", 72, 72, 0, 56, "8", 141, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["UP£", 72, 72, 0xE0, 72, 0xE0, 141, 0xE0, 152, 0],
    ["PGUP", 73, 73, 0, 57, "9", 132, 0, 153, 0],
    [None, None, None, None, None, None, None, None, None, None],
    ["PGUP£", 73, 73, 0xE0, 73, 0xE0, 132, 0xE0, 153, 0],
    ["GRAY-", 74, None, None, 45, "-", None, None, None, None],
    ["LEFT", 75, 75, 0, 52, "4", 115, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["LEFT£", 75, 75, 0xE0, 75, 0xE0, 115, 0xE0, 155, 0],
    ["CENTER", 76, None, None, 53, "5", None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["RIGHT", 77, 77, 0, 54, "6", 116, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["RIGHT£", 77, 77, 0xE0, 77, 0xE0, 116, 0xE0, 157, 0],
    ["GRAY+", 78, None, None, 43, "+", None, None, None, None],
    ["END", 79, 79, 0, 49, "1", 117, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["END£", 79, 79, 0xE0, 79, 0xE0, 117, 0xE0, 159, 0],
    ["DOWN", 80, 80, 0, 50, "2", 145, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["DOWN£", 80, 80, 0xE0, 80, 0xE0, 145, 0xE0, 160, 0],
    ["PGDN", 81, 81, 0, 51, "3", 118, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["PGDN£", 81, 81, 0xE0, 81, 0xE0, 118, 0xE0, 161, 0],
    ["INS", 82, 82, 0, 48, "0", 146, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["INS£", 82, 82, 0xE0, 82, 0xE0, 146, 0xE0, 162, 0],
    ["DEL", 83, 83, 0, 46, ".", 147, 0, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    ["DEL£", 83, 83, 0xE0, 83, 0xE0, 147, 0xE0, 163, 0],
]

keycodes = [
    ["ESC", 1, 27, None, 27, None, None, None, None, None],
    ["1!", 2, 49, "1", 33, "!", None, None, 49, None],
    ["2@", 3, 50, "2", 64, "@", 3, 0, 50, None],
    ["3#", 4, 51, "3", 35, "#", None, None, 51, None],
    ["4$", 5, 52, "4", 36, "$", None, None, 52, None],
    ["5%", 6, 53, "5", 37, "%", None, None, 53, None],
    ["6^", 7, 54, "6", 94, "^", None, None, 54, None],
    ["7&", 8, 55, "7", 38, "&", None, None, 55, None],
    ["8*", 9, 56, "8", 42, "*", None, None, 56, None],
    ["9(", 10, 57, "9", 40, "(", None, None, 57, None],
    ["0)", 11, 48, "0", 41, ")", None, None, 48, None],
    ["-_", 12, 45, "-", 95, "_", None, None, 45, None],
    ["=+", 13, 61, "=", 43, "+", None, None, 61, None],
    ["BKSP", 14, 8, None, 8, None, 127, None, 8, None],
    ["TAB", 15, 9, None, 9, None, 148, 0, None, None],
    ["Q", 16, 113, "q", 81, "Q", 17, "\x11", 113, None],
    ["W", 17, 119, "w", 87, "W", 23, "\x17", 119, None],
    ["E", 18, 101, "e", 69, "E", 5, "\x05", 101, None],
    ["R", 19, 114, "r", 82, "R", 18, "\x12", 114, None],
    ["T", 20, 116, "t", 84, "T", 20, "SO", 116, None],
    ["Y", 21, 121, "y", 89, "Y", 25, "\x19", 121, None],
    ["U", 22, 117, "u", 85, "U", 21, "\x15", 117, None],
    ["I", 23, 105, "i", 73, "I", 9, "\t", 105, None],
    ["O", 24, 111, "o", 79, "O", 15, "\x0f", 111, None],
    ["P", 25, 112, "p", 80, "P", 16, "\x10", 112, None],
    ["[{", 26, 91, "[", 123, "{", 27, "\x1b", 91, None],
    ["]}", 27, 93, "]", 125, "}", 29, "\x1d", 93, None],
    ["ENTER", 28, 13, "\r", 13, "\r", 10, "\x0a", None, None],
    ["ENTER£", 28, 13, "\r", 13, "\r", 10, "\x0a", None, None],
    ["LCTRL", 29, None, None, None, None, None, None, None, None],
    ["RCTRL£", 29, None, None, None, None, None, None, None, None],
    ["A", 30, 97, "a", 65, "A", 1, "\x01", 97, None],
    ["S", 31, 115, "s", 83, "S", 19, "\x13", 115, None],
    ["D", 32, 100, "d", 68, "D", 4, "\x04", 100, None],
    ["F", 33, 102, "f", 70, "F", 6, "\x06", 102, None],
    ["G", 34, 103, "g", 71, "G", 7, "\a", 103, None],
    ["H", 35, 104, "h", 72, "H", 8, "\b", 104, None],
    ["J", 36, 106, "j", 74, "J", 10, "\x0a", 106, None],
    ["K", 37, 107, "k", 75, "K", 11, "\v", 107, None],
    ["L", 38, 108, "l", 76, "L", 12, "\f", 108, None],
    [";:", 39, 59, ";", 58, ":", None, None, 59, None],
    ["'\"", 40, 39, "'", 34, '"', None, None, 39, None],
    ["`~", 41, 96, "`", 126, "~", None, None, 96, None],
    ["L SHIFT", 42, None, None, None, None, None, None, None, None],
    ["\\|", 43, 92, "\\", 124, "|", 28, "\x1c", 92, None],
    ["Z", 44, 122, "z", 90, "Z", 26, "\x1a", 122, None],
    ["X", 45, 120, "x", 88, "X", 24, "\x18", 120, None],
    ["C", 46, 99, "c", 67, "C", 3, "\x03", 99, None],
    ["V", 47, 118, "v", 86, "V", 22, "\x16", 118, None],
    ["B", 48, 98, "b", 66, "B", 2, "\x02", 98, None],
    ["N", 49, 110, "n", 78, "N", 14, "\x0e", 110, None],
    ["M", 50, 109, "m", 77, "M", 13, "\x0d", 109, None],  # Ctrl-m -> \r
    [",<", 51, 44, ",", 60, "<", None, None, 44, None],
    [".>", 52, 46, ".", 62, ">", None, None, 46, None],
    ["/?", 53, 47, "/", 63, "?", None, None, 47, None],
    ["GRAY/£", 53, 47, "/", 63, "?", 149, 0, 164, 0],
    ["R SHIFT", 54, None, None, None, None, None, None, None, None],
    ["PRISC", 55, 42, "*", "PRISC", "✝✝", 16, None, None, None],
    ["L ALT", 56, None, None, None, None, None, None, None, None],
    ["R ALT£", 57, None, None, None, None, None, None, None, None],
    ["SPACE", 57, 32, " ", 32, " ", 32, " ", None, None],
    ["CAPS", 58, None, None, None, None, None, None, None, None],
    ["F1", 59, 59, 0, 84, 0, 94, 0, 104, 0],
    ["F2", 60, 60, 0, 85, 0, 95, 0, 105, 0],
    ["F3", 61, 61, 0, 86, 0, 96, 0, 106, 0],
    ["F4", 62, 62, 0, 87, 0, 97, 0, 107, 0],
    ["F5", 63, 63, 0, 88, 0, 98, 0, 108, 0],
    ["F6", 64, 64, 0, 89, 0, 99, 0, 109, 0],
    ["F7", 65, 65, 0, 90, 0, 100, 0, 110, 0],
    ["F8", 66, 66, 0, 91, 0, 101, 0, 111, 0],
    ["F9", 67, 67, 0, 92, 0, 102, 0, 112, 0],
    ["F10", 68, 68, 0, 93, 0, 103, 0, 113, 0],
    ["F11£", 87, 133, 0xE0, 135, 0xE0, 137, 0xE0, 139, 0xE0],
    ["F12£", 88, 134, 0xE0, 136, 0xE0, 138, 0xE0, 140, 0xE0],
    ["NUM", 69, None, None, None, None, None, None, None, None],
    ["HOME", 71, 71, 0, None, None, 119, 0, None, None],
    [None, None, 55, "7", 71, 0, 119, 0, None, None],
    ["HOME£", 71, 71, 0xE0, 71, 0xE0, 119, 0xE0, 151, 0],
    ["UP", 72, 72, 0, None, None, 141, 0, None, None],
    [None, None, 56, "8", 72, 0, 141, 0, None, None],
    ["UP£", 72, 72, 0xE0, 72, 0xE0, 141, 0xE0, 152, 0],
    ["PGUP", 73, 73, 0, None, None, 132, 0, None, None],
    [None, None, 57, "9", 73, 0, 132, 0, None, None],
    ["PGUP£", 73, 73, 0xE0, 73, 0xE0, 134, 0xE0, 153, 0],
    ["GRAY-", 74, None, None, 45, "-", None, None, None, None],
    ["LEFT", 75, 75, 0, None, None, 115, 0, None, None],
    [None, None, 52, "4", 75, 0, 115, 0, None, None],
    ["LEFT£", 75, 75, 0xE0, 75, 0xE0, 115, 0xE0, 155, 0],
    ["CENTER", 76, None, None, None, None, None, None, None, None],
    [None, None, 53, "5", None, None, None, None, None, None],
    ["RIGHT", 77, 77, 0, None, None, 116, 0, None, None],
    [None, None, 54, "6", 77, 0, 116, 0, None, None],
    ["RIGHT£", 77, 77, 0xE0, 77, 0xE0, 116, 0xE0, 157, 0],
    ["GRAY+", 78, None, None, 43, "+", None, None, None, None],
    ["END", 79, 79, 0, None, None, 117, 0, None, None],
    [None, None, 49, "1", 79, 0, 117, 0, None, None],
    ["END£", 79, 79, 0xE0, 79, 0xE0, 117, 0xE0, 159, 0],
    ["DOWN", 80, 80, 0, None, None, 145, 0, None, None],
    [None, None, 50, "2", 80, 0, 145, 0, None, None],
    ["DOWN£", 80, 80, 0xE0, 80, 0xE0, 145, 0xE0, 160, 0],
    ["PGDN", 81, 81, 0, None, None, 118, 0, None, None],
    [None, None, 51, "3", 81, 0, 118, 0, None, None],
    ["PGDN£", 81, 81, 0xE0, 81, 0xE0, 118, 0xE0, 161, 0],
    ["INS", 82, 82, 0, None, None, 146, 0, None, None],
    [None, None, 48, "0", 82, 0, 146, 0, None, None],
    ["INS£", 82, 82, 0xE0, 82, 0xE0, 146, 0xE0, 162, 0],
    ["DEL", 83, 83, 0, None, None, 147, 0, None, None],
    [None, None, 46, ".", 83, 0, 147, 0, None, None],
    ["DEL£", 83, 83, 0xE0, 83, 0xE0, 147, 0xE0, 163, 0],
]

noms = "base shift ctrl alt".split()

if __name__ == "__main__":
    import textwrap

    text = r"\text{{{}}}".format
    error = r"\color{{red}}{{{}}}".format
    gray = r"\color{{gray}}{{{}}}".format
    green = r"\color{{green}}{{{}}}".format
    to = r"{} \to {}".format

    def repr_text(value):
        return text(
            repr(value)[1:-1]
            .replace("{", r"\{")
            .replace("}", r"\}")
            .replace("$", r"\$")
            .replace(r"\'", "'")
        )

    def error_text(value):
        return error(repr_text(value))

    class Wrapper:
        def __init__(self, new, old):
            self.new = new
            self.old = old

        def __str__(self):
            if isinstance(self.new, int) or isinstance(self.old, int):
                if self.new == self.old:
                    return gray(text(self.old))
                else:
                    return to(error_text(self.old), green(text(self.new)))
            elif self.new == self.old:
                if self.new is None:
                    return ""
                else:
                    return repr_text(self.old)
            elif self.new is None:
                return error_text(self.old)
            elif self.old is None:
                return green(repr_text(self.new))
            else:
                return to(error_text(self.old), green(repr_text(self.new)))

    def read_table(table):
        for name, scan, *groups in table:
            codes = []
            for code, other in zip(*[iter(groups)] * 2):
                if code is None:
                    if other is None:
                        codes.append(None)
                    else:
                        print("code: None other: ??? - {}".format(other))
                        codes.append(str(other))
                elif isinstance(code, str):
                    print("code: str - {} {}".format(code, other))
                    codes.append(
                        "".join([str(i) for i in (other, code) if i is not None])
                    )
                elif other is None or isinstance(other, str):
                    codes.append(chr(code))
                else:
                    codes.append("".join(chr(i) for i in (other, code)))
            yield (name, scan, *codes)

    def read_tables(n, o):
        for n_values, o_values in zip(read_table(n), read_table(o)):
            yield [
                Wrapper(n_value, o_value)
                for n_value, o_value in zip(n_values, o_values)
            ]

    fmt = r"""
$$
\begin{{array}}{{l|r|l|l|l|l}}
  \textrm{{Name}} &
  \textrm{{Scan Code}} &
  \textrm{{Base}} &
  \textrm{{Shift}} &
  \textrm{{Ctrl}} &
  \textrm{{Alt}} \\
  \hline
  
{}\\

\end{{array}}
$$
"""

    def format_(rows):
        values = "\\\\\n".join("&".join(map(str, row)) for row in rows)
        return textwrap.indent(fmt.format(textwrap.indent(values, "  ")), " " * 4)

    def chunks(l, n):
        l = list(l)
        for i in range(0, len(l), n):
            yield l[i : i + n]

    for chunk in chunks(read_tables(keycodes, _keycodes), 40):
        print(format_(chunk))
