class Memory:                               
    def __init__(self):
        self.scopes = [({}, "global")]

    def get(self, name):
        for scope in self.scopes[::-1]:
            res = scope[0].get(name)
            if res is not None:
                return res

        return None

    def put(self, name, value):
        for scope in self.scopes[::-1]:
            if name in scope[0]:
                scope[0][name] = value
                return

        self.scopes[-1][0][name] = value

    def pushScope(self, name):
        self.scopes.append(({}, name))

    def popScope(self):
        self.scopes.pop()
        