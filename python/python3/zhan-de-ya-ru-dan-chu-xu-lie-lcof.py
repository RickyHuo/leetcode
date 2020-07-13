class Solution:
    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:

        stack = []
        # for i in enumerate
        while len(popped) > 0:
            top = popped.pop(0)
            if len(stack) > 0 and stack[-1] == top:
                stack.pop()

            else:
                while len(pushed) > 0:
                    tail = pushed.pop(0)
                    if tail == top:
                        break
                    else:
                        stack.append(tail)
            if len(pushed) + len(stack) != len(popped):
                return False
        return True

if __name__ == '__main__':
    Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2])