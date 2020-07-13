class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        self.min = []

    def push(self, x: int) -> None:
        self.val.append(x)
        if len(self.min) >= 1:
            min_val = min(self.getMin(), x)
        else:
            min_val = x
        self.min.append(min_val)

    def pop(self) -> None:
        self.min.pop()
        self.val.pop()

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()