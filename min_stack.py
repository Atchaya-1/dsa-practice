class MinStack:
    
    def __init__(self):
      self.stack = []
      self.minstac = []
    def push(self, value: int) -> None:
        self.stack.append(value)
        value = min(value,self.minstac[-1] if self.minstac else value)
        self.minstac.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minstac.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstac[-1]


minStack =  MinStack()

minStack.push(-1)
minStack.push(0)
minStack.push(-4)
minStack.push(-6)
minStack.push(-2)
minStack.getMin()
minStack.pop()
minStack.top() 
minStack.getMin()
print(minStack.getMin())