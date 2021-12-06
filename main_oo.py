#!/usr/bin/env python3

import sys
import scanner_oo
import Mparser
import TreePrinter
from TypeChecker import TypeChecker

if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print(f"Cannot open {filename} file")
        sys.exit(1)

    text = file.read()
    parser = Mparser.parser

    lexer = scanner_oo.Scanner()
    lexer.build()
    ast = parser.parse(text, lexer=lexer)
    # ast.printTree(0)
    typeChecker = TypeChecker()   
    typeChecker.visit(ast)   # or alternatively ast.accept(typeChecker)
