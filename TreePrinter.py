from __future__ import print_function
import AST

def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Node)
    def indent(self, indent):
        print("|   " * indent, end="")

    @addToClass(AST.BinExpr)
    def printTree(self, indent):
        self.indent(indent)
        print(self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.BinCond)
    def printTree(self, indent):
        self.indent(indent)
        print(self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Assign)
    def printTree(self, indent):
        self.indent(indent)
        print(self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.IfCond)
    def printTree(self, indent):
        self.indent(indent)
        print("IF")
        self.cond.printTree(indent + 1)
        self.if_body.printTree(indent + 1)
        if self.else_body is not None:
            self.indent(indent)
            print("ELSE")
            self.else_body.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent):
        self.indent(indent)
        print("WHILE")
        self.cond.printTree(indent + 1)
        self.body.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self, indent):
        self.indent(indent)
        print("FOR")
        self.begin.printTree(indent + 1)
        self.end.printTree(indent + 1)
        self.body.printTree(indent + 1)
    
    @addToClass(AST.Break)
    def printTree(self, indent=0):
        self.indent(indent)
        print("BREAK")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        self.indent(indent)
        print("CONTINUE")
    
    @addToClass(AST.Return)
    def printTree(self, indent=0):
        self.indent(indent)
        print("RETURN")
        if self.expr is not None:
            self.expr.printTree(indent+1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        self.indent(indent)
        print("PRINT")
        for expr in self.exprs:
            expr.printTree(indent + 1)
    

    @addToClass(AST.Transpose)
    def printTree(self, indent=0):
        self.indent(indent)
        print("TRANSPOSE")
        self.arg.printTree(indent + 1)

    @addToClass(AST.Fun)
    def printTree(self, indent=0):
        self.indent(indent)
        print(self.fun)
        self.arg.printTree(indent + 1)
    

    @addToClass(AST.Matrix)
    def printTree(self, indent):
        self.indent(indent)
        print("MATRIX")
        for row in self.matrix:
            self.indent(indent + 1)
            print("ROW")
            for expr in row:
                expr.printTree(indent + 2)

    
    @addToClass(AST.Uminus)
    def printTree(self, indent=0):
        self.indent(indent)
        print("-")
        self.arg.printTree(indent + 1)

    @addToClass(AST.ID)
    def printTree(self, indent):
        self.indent(indent)
        print(self.id)
        
    @addToClass(AST.LValue)
    def printTree(self, indent):
        self.id.printTree(indent)
        if self.index is not None:
            self.indent(indent)
            print("LIST")
            for expr in self.index:
                expr.printTree(indent + 1)

    @addToClass(AST.String)
    def printTree(self, indent=0):
        self.indent(indent)
        print("STRING")
        self.indent(indent + 1)
        print(self.string)
    
    @addToClass(AST.Statements)
    def printTree(self, indent):
        for stmt in self.stmts:
            stmt.printTree(indent)

    @addToClass(AST.IntNum)
    def printTree(self, indent):
        self.indent(indent)
        print(self.value)
    
    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        self.indent(indent)
        print(self.value)
    
    @addToClass(AST.Program)
    def printTree(self, indent):
        for stmt in self.stmts:
            stmt.printTree(0)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
