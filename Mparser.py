#!/usr/bin/python

import scanner_oo
import AST
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
    ('left', "'")
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : stmts_opt"""
    p[0] = AST.Program(p[1])

def p_stmts_opt(p):
    """stmts_opt : stmts
                 | """
    p[0] = p[1] if len(p) > 1 else None

def p_stmts(p):
    """stmts : stmts stmt
             | stmt"""
    p[0] = p[1] + [p[2]] if len(p) > 2 else [p[1]]

def p_stmt_empty(p):
    """stmt : ';'"""
            
def p_stmts_grp(p):
    """stmt : '{' stmts '}'"""
    p[0] = AST.Statements(p[2])

def p_id(p):
    """id : ID"""
    p[0] = AST.ID(p[1])

def p_lvalue(p):
    """lvalue : id
              | id list"""
    p[0] = AST.LValue(p[1], p[2] if len(p) > 2 else None)

def p_assignment(p):
    """stmt : lvalue '=' expr ';'
            | lvalue ADDASSIGN expr ';'
            | lvalue SUBASSIGN expr ';'
            | lvalue MULASSIGN expr ';'
            | lvalue DIVASSIGN expr ';'"""
    p[0] = AST.Assign(p[2], p[1], p[3])

def p_expr_binop(p):
    """expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
            | expr DOTADD expr
            | expr DOTSUB expr
            | expr DOTMUL expr
            | expr DOTDIV expr"""
    p[0] = AST.BinExpr(p[2], p[1], p[3])

def p_expr_lit(p):
    """expr : FLOATNUM
            | INTNUM"""
    p[0] = AST.IntNum(p[1]) if type(p[1]) == int else AST.FloatNum(p[1])

def p_expr_id(p):
    """expr : id"""
    p[0] = p[1]

def p_expr_str(p):
    """expr : STR"""
    p[0] = AST.String(p[1])

def p_expr_grp(p):
    """expr : '(' expr ')'"""
    p[0] = p[2]

def p_uminus(p):
    """expr : '-' expr %prec UMINUS"""
    p[0] = AST.Uminus(p[2])

def p_transpose(p):
    """expr : expr '\\''"""
    p[0] = AST.Transpose(p[1])

def p_cond(p):
    """cond : expr '<' expr
            | expr '>' expr
            | expr LE expr
            | expr GE expr
            | expr EQ expr
            | expr NEQ expr"""
    p[0] = AST.BinCond(p[2], p[1], p[3])

def p_literal_matrix(p):
    """expr : '[' lists ']'"""
    p[0] = AST.Matrix(p[2])

def p_lists(p):
    """lists : list
             | lists ',' list"""
    p[0] = p[1] + [p[3]] if len(p) > 3 else [p[1]]

def p_list(p):
    """list : '[' seq ']'"""
    p[0] = p[2]

def p_seq(p):
    """seq : expr
           | seq ',' expr"""
    p[0] = p[1] + [p[3]] if type(p[1]) == list else [p[1]]

def p_fun(p):
    """fun : ZEROS 
           | EYE
           | ONES"""
    p[0] = p[1]

def p_funcall(p):
    """expr : fun '(' expr ')'"""
    p[0] = AST.Fun(p[1], p[3])

def p_while(p):
    """stmt : WHILE '(' cond ')' stmt"""
    p[0] = AST.While(p[3], p[5])

def p_for(p):
    """stmt : FOR id '=' expr ':' expr stmt"""
    p[0] = AST.For(p[2], p[4], p[6], p[7])

def p_if(p):
    """stmt : IF '(' cond ')' stmt %prec IFX
            | IF '(' cond ')' stmt ELSE stmt"""
    p[0] = AST.IfCond(p[3], p[5], p[7] if len(p) > 7 else None)

def p_control(p):
    """stmt : BREAK ';'
            | CONTINUE ';'
            | RETURN expr ';'"""
    if p[1] == 'break':
        p[0] = AST.Break()
    elif p[1] == 'continue':
        p[0] = AST.Continue()
    else:
        p[0] = AST.Return(p[2])

def p_print(p):
    """stmt : PRINT seq ';'"""
    p[0] = AST.Print(p[2])


# ID = (5 + 5)
# ID2 = [[2, 1], [3, 7]]

# ID = [[1, 3, 5]] 1x3
# ID = [2,3,4]
# ID[2];

# ID[5, 3] # ID '[' expr ',' expr ']'
         # ID list
# [[2,3]][2,3]

parser = yacc.yacc()
