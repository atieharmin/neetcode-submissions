class MinStack:

    def __init__(self):
        self.s = []
        self.pref = []
    def push(self, val: int) -> None:
        if len(self.s) == 0:
            self.pref.append(val)
        else:
            self.pref.append(min(self.pref[-1],val))
        self.s.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.pref.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.pref[-1]
        
        
