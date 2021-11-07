#!/usr/bin/env python3

import sys
import scanner_oo
import Mparser

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
    parser.parse(text, lexer=lexer)
    # lexer = scanner_oo.Scanner()
    # lexer.build()

    # # Give the lexer some input
    # lexer.input(text)

    # # Tokenize
    # while True:
    #     tok = lexer.token()
    #     if not tok: 
    #         break      # No more input
    #     print(f"({tok.lineno}): {tok.type}({tok.value})")
