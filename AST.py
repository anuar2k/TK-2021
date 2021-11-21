class Node(object):
    pass

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class BinCond(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Assign(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class IfCond(Node):
    def __init__(self, cond, if_body, else_body=None):
        self.cond = cond
        self.if_body = if_body
        self.else_body = else_body

class While(Node):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class For(Node):
    def __init__(self, var, begin, end, body):
        self.var = var
        self.begin = begin
        self.end = end
        self.body = body

class Break(Node):
    def __init__(self):
        pass

class Continue(Node):
    def __init__(self):
        pass

class Return(Node):
    def __init__(self, expr=None):
        self.expr = expr

class Print(Node):
    def __init__(self, exprs):
        self.exprs = exprs

class Transpose(Node):
    def __init__(self, arg):
        self.arg = arg

class Uminus(Node):
    def __init__(self, arg):
        self.arg = arg

class Fun(Node):
    def __init__(self, fun, arg):
        self.fun = fun
        self.arg = arg

class Matrix(Node):
    def __init__(self, matrix):
        self.matrix = matrix

class ID(Node):
    def __init__(self, id):
        self.id = id

class LValue(Node):
    def __init__(self, id, index=None):
        self.id = id
        self.index = index

class String(Node):
    def __init__(self, string):
        self.string = string
        
class Statements(Node):
    def __init__(self, stmts):
        self.stmts = stmts

class IntNum(Node):
    def __init__(self, value):
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value

class Program(Node):
    def __init__(self, stmts):
        self.stmts = stmts

# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
      
