class SymbolTable:
    def __init__(self):
        self.scopes = [(set(), "global")]

    def put(self, name):
        self.scopes[-1][0].add(name)

    def get(self, name):
        for scope in self.scopes[::-1]:
            if name in scope[0]:
                return name

        return None

    def getScope(self, name):
        for scope in self.scopes[::-1]:
            if scope[1] == name:
                return scope

        return None

    def pushScope(self, name):
        self.scopes.append((set(), name))

    def popScope(self):
        self.scopes.pop()
