class Solution:
    def __init__(self):
        self.stack = []

    def evalRPN(self, tokens: [str]) -> int:
        for i in tokens:
            if i in ["-", "+", "*", "/"]:
                right = self.stack.pop()
                left = self.stack.pop()
                if i == "+":
                    self.stack.append(right + left)
                elif i == "-":
                    self.stack.append(left - right)
                elif i == "*":
                    self.stack.append(left * right)
                elif i == "/":
                    self.stack.append(int(left / right))
            else:
                self.stack.append(int(i))
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return 0


if __name__ == "__main__":
    s = Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(s)