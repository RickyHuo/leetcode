# encoding: utf-8


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        items = []
        for i in s:
            if i == ' ':
                continue
            elif i == '(' or i == '[' or i == '{':
                items.append(i)
            elif len(items) == 0:
                return False
            else:
                item = items.pop()

                if not self.equals(item, i):
                    return False

        if len(items) == 0:
            return True
        else:
            return False

    def equals(self, left, rigth):
        if left == '(' and rigth == ')':
            return True
        elif left == '[' and rigth == ']':
            return True
        elif left == '{' and rigth == '}':
            return True
        else:
            return False


if __name__ == '__main__':

    # 利用栈 先入后出的特点
    print Solution().isValid("{ ]")

