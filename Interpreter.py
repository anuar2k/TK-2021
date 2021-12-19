
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
        self.op_dict = {
            '+' : lambda x, y: x + y,
            '-' : lambda x, y: x - y,
            '*' : lambda x, y: x * y, 
            '/' : lambda x, y: x / y,
            '.+': lambda x, y: np.add(x,y),
            '.-': lambda x, y: np.subtract(x,y),
            '.*': lambda x, y: np.multiply(x,y),
            './': lambda x, y: np.divide(x,y),
            "'": lambda x: np.transpose(x),
            "==": lambda x, y: x == y,
            "!=": lambda x, y: x != y,
            ">=": lambda x, y: x >= y,
            "<=": lambda x, y: x <= y,
            '<': lambda x, y: x < y,
            '>': lambda x, y: x > y,
            "=": lambda var, x: self.memory.put(var, x),
            "+=": lambda var, x, y: self.memory.put(var, x + y),
            "-=": lambda var, x, y: self.memory.put(var, x - y),
            "*=": lambda var, x, y: self.memory.put(var, x * y),
            "/=": lambda var, x, y: self.memory.put(var, x / y),
            "zeros": lambda s: np.zeros((s,s)),
            "ones": lambda s: np.ones((s,s)),
            "eye": lambda s: np.eye(s),
        }

    @on('node')
    def visit(self, node):
        pass

    # @when(AST.BinOp)
    # def visit(self, node):
    #     r1 = node.left.accept(self)
    #     r2 = node.right.accept(self)
    #     # try sth smarter than:
    #     # if(node.op=='+') return r1+r2
    #     # elsif(node.op=='-') ...
    #     # but do not use python eval

    # @when(AST.Assignment)
    # def visit(self, node):
    #     pass
    # #
    # #

    # # simplistic while loop interpretation
    # @when(AST.WhileInstr)
    # def visit(self, node):
    #     r = None
    #     while node.cond.accept(self):
    #         r = node.body.accept(self)
    #     return r

    @when(AST.Node)
    def visit(self, node):
        pass

    @when(AST.BinExpr)
    def visit(self, node):
        return self.op_dict[node.op](self.visit(node.left), self.visit(node.right))

    @when(AST.BinCond)
    def visit(self, node):
        return self.op_dict[node.op](self.visit(node.left), self.visit(node.right))

    @when(AST.Assign)
    def visit(self, node):
        # TODO: assign
        pass

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
                self.memory.popScope()
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
        return self.op_dict["'"](self.visit(node.arg))

    @when(AST.Fun)
    def visit(self, node):
        return self.op_dict[node.fun](self.visit(node.arg))

    @when(AST.Matrix)
    def visit(self, node):
        return np.array(node.matrix)
    
    @when(AST.Uminus)
    def visit(self, node):
        return self.op_dict["*"](self.visit(node.arg), -1)

    @when(AST.ID)
    def visit(self, node):
        value = self.memory.get(node.id)
        if node.index is not None:
            x, y = node.index
            return value[x, y]
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
