import ply.lex as lex
import sys

class Scanner():
    t_ignore = " \t"
    literals = "+-*/=<>()[]{}:',;"

    _reserved = {
        "if": "IF",
        "else": "ELSE",
        "for": "FOR",
        "while": "WHILE",
        "break": "BREAK",
        "continue": "CONTINUE",
        "return": "RETURN",
        "eye": "EYE",
        "zeros": "ZEROS",
        "ones": "ONES",
        "print": "PRINT"
    }
    
    tokens = [
        "DOTADD",
        "DOTSUB",
        "DOTMUL",
        "DOTDIV",
        "ADDASSIGN",
        "SUBASSIGN",
        "MULASSIGN",
        "DIVASSIGN",
        "LE",
        "GE",
        "NEQ",
        "EQ",
        "ID",
        "INTNUM",
        "FLOATNUM",
        "STR"
    ] + list(_reserved.values())

    t_DOTADD = r"\.\+"
    t_DOTSUB = r"\.-"
    t_DOTMUL = r"\.\*"
    t_DOTDIV = r"\./"
    t_ADDASSIGN = r"\+="
    t_SUBASSIGN = r"-="
    t_MULASSIGN = r"\*="
    t_DIVASSIGN = r"/="
    t_LE = r"<="
    t_GE = r">="
    t_NEQ = r"!="
    t_EQ = r"=="
    t_STR = r"\".*\""
    t_INTNUM = r"\d+"
    t_FLOATNUM = r"[+-]?(\d+[.](\d*)?([eE][+-]?\d+)?|[.]\d+([eE][+-]?\d+)?)"

    def t_ID(self, t):
        r"[a-zA-Z_]\w*"
        t.type = self._reserved.get(t.value, "ID")
        return t

    def t_COMMENT(self, t):
        r"\#.*"

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Illegal character {t.value[0]} at line {t.lexer.lineno}", file=sys.stderr)

        t.lexer.skip(1)

    def build(self):
        self.lexer = lex.lex(object=self)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        return self.lexer.token()
