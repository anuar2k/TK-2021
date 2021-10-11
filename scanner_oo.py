import ply.lex as lex

# https://github.com/PrzemekBurczyk/PLY/blob/master/scanner.py
class Scanner():
    t_ignore = " \t"
    literals = "+-*/=<>()[]{}:',;"
    tokens = (
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
        "IF",
        "ELSE",
        "FOR",
        "BREAK",
        "CONTINUE",
        "RETURN",
        "EYE",
        "ZEROS",
        "PRINT"
    )

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_COMMENT(self, t):
        r"\#.*"

    _reserved = {
        "if": "IF",
        "else": "ELSE",
        "for": "FOR",
        "break": "BREAK",
        "continue": "CONTINUE",
        "return": "RETURN",
        "eye": "EYE",
        "zeros": "ZEROS",
        "print": "PRINT"
    }

    def build(self):
        self.lexer = lex.lex(object=self)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        return self.lexer.token()

    t_DOTADD = r"\.\+"
    t_DOTSUB = r"\.-"
    t_DOTMUL = r"\.\*"
    t_DOTDIV = r"\./"
    t_ADDASSIGN = r"\+="
    t_SUBASSIGN = r"-="
    t_MULASSIGN = r"\*="
    t_DIVASSIGN = r"=/"
    t_LE = r"<="
    t_GE = r">="
    t_NEQ = r"!="
    t_EQ = r"=="

