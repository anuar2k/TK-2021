#!/usr/bin/python

import scanner_oo
import ply.yacc as yacc


tokens = scanner_oo.Scanner.tokens

precedence = (
    ("nonassoc", "IFX"),
    ("nonassoc", "ELSE"),
    ("left", '+', '-'),
    ("left", '*', '/'),
    ("left", "DOTADD", "DOTSUB"),
    ("left", "DOTMUL", "DOTDIV"),
    ('right', 'UMINUS'),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : stmts_opt"""

def p_stmts_opt(p):
    """stmts_opt : stmts
                 | """

def p_stmts(p):
    """stmts : stmts stmt
             | stmt"""

def p_stmt_empty(p):
    """stmt : ';'"""
            
def p_stmts_grp(p):
    """stmt : '{' stmts '}'"""

def p_assignment(p):
    """stmt : ID '=' expr ';'
            | ID ADDASSIGN expr ';'
            | ID SUBASSIGN expr ';'
            | ID MULASSIGN expr ';'
            | ID DIVASSIGN expr ';'"""

def p_expr_binop(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTMUL expr
            | expr DOTDIV expr"""
# zw
def p_expr_lit(p):
    """expr : FLOATNUM
            | INTNUM"""

def p_expr_id(p):
    """expr : ID"""

def p_expr_str(p):
    """expr : STR"""

def p_expr_grp(p):
    """expr : '(' expr ')'"""

def p_uminus(p):
    """expr : '-' expr %prec UMINUS"""

def p_transpose(p):
    """expr : expr '\\''"""

def p_cond(p):
    """cond : expr '<' expr
            | expr '>' expr
            | expr LE expr
            | expr GE expr
            | expr EQ expr
            | expr NEQ expr"""

def p_literal_matrix(p):
    """expr : '[' lists ']'"""

def p_lists(p):
    """lists : list
             | lists ',' list"""

def p_list(p):
    """list : '[' seq ']'"""

def p_seq(p):
    """seq : expr
           | seq ',' expr"""

def p_fun(p):
    """fun : ZEROS 
           | EYE
           | ONES"""

def p_funcall(p):
    """expr : fun '(' expr ')'"""

def p_while(p):
    """stmt : WHILE '(' cond ')' stmt"""

def p_for(p):
    """stmt : FOR ID '=' expr ':' expr stmt"""

def p_if(p):
    """stmt : IF '(' cond ')' stmt %prec IFX
            | IF '(' cond ')' stmt ELSE stmt"""

def p_control(p):
    """stmt : BREAK ';'
            | CONTINUE ';'
            | RETURN expr ';'"""

def p_print(p):
    """stmt : PRINT seq ';'"""

def p_access(p):
    """stmt : ID list '=' expr"""

# ID = (5 + 5)
# ID2 = [[2, 1], [3, 7]]

# ID = [[1, 3, 5]] 1x3
# ID = [2,3,4]
# ID[2];

# ID[5, 3] # ID '[' expr ',' expr ']'
         # ID list
# [[2,3]][2,3]

parser = yacc.yacc()
