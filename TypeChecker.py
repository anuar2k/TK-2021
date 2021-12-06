#!/usr/bin/python

import AST
from SymbolTable import SymbolTable

# sprawdzenie IDków (występowanie w scope) - globalnie
# sprawdzenie return, continue, break w odpowiednim scope
# sprawdzenie wymiarowości macierzy
# sprawdzenie, czy lista indeksujaca ma dlugosc 2

class NodeVisitor:
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method)
        if visitor is not None:
            return visitor(node)
        return None

class TypeChecker(NodeVisitor):
    def __init__(self):
        self.table = SymbolTable()

    def visit_BinExpr(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_BinCond(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_Assign(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_IfCond(self, node):
        self.table.pushScope("normal")
        self.visit(node.if_body)
        self.table.popScope()

        if node.else_body is not None:
            self.table.pushScope("normal")
            self.visit(node.else_body)
            self.table.popScope()

    def visit_While(self, node):
        self.visit(node.cond)

        self.table.pushScope("loop")
        self.visit(node.body)
        self.table.popScope()

    def visit_For(self, node):
        # self.visit(node.var) - don't visit, will be added in next scope
        self.visit(node.begin)
        self.visit(node.end)

        self.table.pushScope("loop")
        self.table.put(node.var.id)
        self.visit(node.body)
        self.table.popScope()

    def visit_Break(self, node):
        if self.table.getScope("loop") is None:
            print("break outside of loop")

    def visit_Continue(self, node):
        if self.table.getScope("loop") is None:
            print("continue outside of loop")

    def visit_Return(self, node):
        self.visit(node.expr)

    def visit_Print(self, node):
        for expr in node.exprs:
            self.visit(expr)

    def visit_Transpose(self, node):
        self.visit(node.arg)

    def visit_Uminus(self, node):
        self.visit(node.arg)

    def visit_Fun(self, node):
        self.visit(node.arg)

    def visit_Matrix(self, node):
        n = len(node.matrix)
        for row in node.matrix[1:]:
            if len(row) != n:
                print("row length not matching")
            for val in row:
                self.visit(val)

    def visit_ID(self, node):
        if self.table.get(node.id) is None:
            print(f"unknown variable: {node.id}")

    def visit_LValue(self, node):
        if node.index is not None:
            if len(node.index) != 2:
                print("expected len of index equal to 2")
            self.visit(node.id) # check assignment to existing var
            for idx in node.index:
                self.visit(idx)
        else:
            # may create new variable
            self.table.put(node.id.id)

    def visit_String(self, node):
        pass

    def visit_Statements(self, node):
        self.table.pushScope("normal")
        for stmt in node.stmts:
            self.visit(stmt)
        self.table.popScope()

    def visit_IntNum(self, node):
        pass

    def visit_FloatNum(self, node):
        pass

    def visit_Program(self, node):
        for stmt in node.stmts:
            self.visit(stmt)
