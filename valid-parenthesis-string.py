class Solution(object):

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        star_stack = []

        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ' ':
                continue
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if len(stack) > 0:
                    stack.pop()
                elif len(star_stack) > 0:
                    star_stack.pop()
                else:
                    return False

        return self.judge(stack, star_stack)

    @staticmethod
    def judge(left, star):
        if len(left) == 0:
            return True
        elif len(star) == 0:
            return False
        elif len(star) < len(left):
            return False
        else:
            for i in star[::-1]:
                if i > left[-1]:
                    left.pop()
                    if len(left) == 0:
                        return True
            return False


if __name__ == '__main__':
    print Solution().checkValidString("(((******))")
