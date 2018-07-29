class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if self.backspaceStr(S) == self.backspaceStr(T):
            return True
        else:
            return False

    def backspaceStr(self, s):
        items = []
        for i in s:
            if i != '#':
                items.append(i)
            else:
                if len(items):
                    items.pop()
                else:
                    continue
        return items


if __name__ == '__main__':
    print Solution().backspaceCompare("#a#c", "a##c")