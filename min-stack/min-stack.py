class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.min_v = None
        

    def push(self, val: int) -> None:
        if self.min_v is None or self.min_v > val:
            self.min_v = val
        self.stack1.append(val)
        

    def pop(self) -> None:
        if self.min_v == self.stack1[-1]:
            self.stack1.pop()
            self.min_v = math.inf
            for _ in range(len(self.stack1)):
                self.min_v = min(self.min_v,self.stack1[-1])
                self.stack2.append(self.stack1.pop())
            for _ in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())
        else:
            self.stack1.pop()
        

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        return self.min_v
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()