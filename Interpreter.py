import AST
from Memory import *
from Exceptions import  *
from visit import *
import sys

import numpy as np

sys.setrecursionlimit(10000)

class Interpreter(object):
    def __init__(self):
        self.memory = Memory()
        self.numeric_argset = {
            (int, int),
            (int, float),
            (float, int),
            (float, float),
            (int, np.ndarray),
            (np.ndarray, int),
            (float, np.ndarray),
            (np.ndarray, float)
        }
        self.mul_argset = self.numeric_argset | {(str, int)}
        self.mat_argset = {(np.ndarray, np.ndarray)}
        self.bool_argset = {
            (int, int),
            (int, float),
            (float, int),
            (float, float),
            (np.ndarray, np.ndarray)
        }
        self.transpose_argset = ((np.ndarray,))
        self.fun_argset = {(int,)}

        self.argsets = {
            '+' :    self.numeric_argset,
            '-' :    self.numeric_argset,
            '*' :    self.mul_argset, 
            '/' :    self.numeric_argset,
            '.+':    self.mat_argset,
            '.-':    self.mat_argset,
            '.*':    self.mat_argset,
            './':    self.mat_argset,
            "==":    self.bool_argset,
            "!=":    self.bool_argset,
            ">=":    self.bool_argset,
            "<=":    self.bool_argset,
            '<':     self.bool_argset,
            '>':     self.bool_argset,
            "'":     self.transpose_argset,
            "zeros": self.fun_argset,
            "ones":  self.fun_argset,
            "eye":   self.fun_argset,
        }

        self.ops = {
            '+' :    lambda x, y: x + y,
            '-' :    lambda x, y: x - y,
            '*' :    lambda x, y: x * y, 
            '/' :    lambda x, y: x / y,
            '.+':    lambda x, y: np.add(x,y),
            '.-':    lambda x, y: np.subtract(x,y),
            '.*':    lambda x, y: np.multiply(x,y),
            './':    lambda x, y: np.divide(x,y),
            "==":    lambda x, y: x == y,
            "!=":    lambda x, y: x != y,
            ">=":    lambda x, y: x >= y,
            "<=":    lambda x, y: x <= y,
            '<':     lambda x, y: x < y,
            '>':     lambda x, y: x > y,
            "'":     lambda x: np.transpose(x),
            "zeros": lambda s: np.zeros((s,s)),
            "ones":  lambda s: np.ones((s,s)),
            "eye":   lambda s: np.eye(s),
        }

    def evaluate(self, op, args):
        types = tuple(type(arg) for arg in args)
        if types not in self.argsets[op]:
            raise ArgumentException()
        
        return self.ops[op](*args)

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Node)
    def visit(self, node):
        pass

    @when(AST.BinExpr)
    def visit(self, node):
        return self.evaluate(node.op, (self.visit(node.left), self.visit(node.right)))

    @when(AST.BinCond)
    def visit(self, node):
        return self.evaluate(node.op, (self.visit(node.left), self.visit(node.right)))

    @when(AST.Assign)
    def visit(self, node):
        to_assign = self.visit(node.right)
        if node.op == '=':
            if node.left.id.index is not None:
                x_src, y_src = node.left.id.index
                subs_src = self.memory.get(node.left.id.id)
                if type(subs_src) != np.ndarray:
                    raise ArgumentException()
                subs = np.copy(subs_src)

                x, y = self.visit(x_src), self.visit(y_src)
                if type(x) != int:
                    raise ArgumentException()
                if type(y) != int:
                    raise ArgumentException()
                if type(to_assign) not in { int, float }:
                    raise ArgumentException()

                subs[x, y] = to_assign
                to_assign = subs
        else:
            if node.left.id.index is None:
                to_assign = self.evaluate(node.op[0], (self.memory.get(node.left.id.id), to_assign))
            else:
                x_src, y_src = node.left.id.index
                subs_src = self.memory.get(node.left.id.id)
                if type(subs_src) != np.ndarray:
                    raise ArgumentException()
                subs = np.copy(subs_src)

                x, y = self.visit(x_src), self.visit(y_src)
                if type(x) != int:
                    raise ArgumentException()
                if type(y) != int:
                    raise ArgumentException()
                if type(to_assign) not in { int, float }:
                    raise ArgumentException()

                subs[x, y] = self.evaluate(node.op[0], (subs[x, y], to_assign))
                to_assign = subs

        self.memory.put(node.left.id.id, to_assign)

    @when(AST.IfCond)
    def visit(self, node):
        if self.visit(node.cond):
            try:
                self.memory.pushScope("normal")
                self.visit(node.if_body)
            finally:
                self.memory.popScope()
        else:
            if node.else_body is not None:
                try:
                    self.memory.pushScope("normal")
                    self.visit(node.else_body)
                finally:
                    self.memory.popScope()

    @when(AST.While)
    def visit(self, node):
        while self.visit(node.cond):
            try:
                self.memory.pushScope("loop")
                self.visit(node.body)
            except ContinueException:
                pass
            except BreakException:
                break
            finally:
                self.memory.popScope()

    @when(AST.For)
    def visit(self, node):
        begin = self.visit(node.begin)
        end = self.visit(node.end)

        for i in range(begin, end):
            try:
                self.memory.pushScope("loop")
                self.memory.put(node.var.id, i)
                self.visit(node.body)
            except ContinueException:
                pass
            except BreakException:
                break
            finally:
                self.memory.popScope()
    
    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()
    
    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(self.visit(node.expr))

    @when(AST.Print)
    def visit(self, node):
        print(", ".join(str(self.visit(expr)) for expr in node.exprs))

    @when(AST.Transpose)
    def visit(self, node):
        return self.evaluate("'", (self.visit(node.arg),))

    @when(AST.Fun)
    def visit(self, node):
        return self.evaluate(node.fun, (self.visit(node.arg),))

    @when(AST.Matrix)
    def visit(self, node):
        return np.array(node.matrix)
    
    @when(AST.Uminus)
    def visit(self, node):
        return self.evaluate("*", (self.visit(node.arg), 1))

    @when(AST.ID)
    def visit(self, node):
        value = self.memory.get(node.id)
        if node.index is not None:
            x, y = node.index
            return value[self.visit(x), self.visit(y)]
        else:
            return value
        
    @when(AST.LValue)
    def visit(self, node):
        # TODO: assignment logic, etc.
        pass

    @when(AST.String)
    def visit(self, node):
        return node.string
    
    @when(AST.Statements)
    def visit(self, node):
        try:
            self.memory.pushScope("normal")
            for stmt in node.stmts:
                self.visit(stmt)
        finally:
            self.memory.popScope()

    @when(AST.IntNum)
    def visit(self, node):
        return node.value
    
    @when(AST.FloatNum)
    def visit(self, node):
        return node.value
    
    @when(AST.Program)
    def visit(self, node):
        try:
            for stmt in node.stmts:
                self.visit(stmt)
        except ReturnValueException as rve:
            print(f"Program returned value {rve.value}")
