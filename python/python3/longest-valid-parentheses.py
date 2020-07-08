class Solution:
    def __init__(self):
        self.stack = []
        self.max = 0

    def longestValidParentheses(self, s: str) -> int:
        fin = 0
        for i, j in enumerate(s):
            if j == "(":
                self.stack.append(i)
            elif j == ")":
                if len(self.stack) == 0:
                    fin = i + 1
                else:
                    self.stack.pop()
                    if len(self.stack) == 0:
                        self.max = max(self.max, i + 1 - fin)
                    else:
                        self.max = max(self.max, i - self.stack[-1])

        return self.max


if __name__ == '__main__':
    s = Solution().longestValidParentheses("))))()()())((")
    print(s)
    s = Solution().longestValidParentheses("((())(")
    print(s)
    s = Solution().longestValidParentheses(")()())")
    print(s)
    s = Solution().longestValidParentheses("()()")
    print(s)
    s = Solution().longestValidParentheses("(()()")
    print(s)