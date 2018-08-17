class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        for i in range(n):
            self.search([i], range(0, i) + range(i + 1, n), n, res)

        return res

    def search(self, prefix, postfix, n, res):
        if self.legal(prefix):
            if len(prefix) == n:
                print prefix
                res.append(self.format(prefix))
            else:
                for i in range(len(postfix)):
                    self.search(prefix + [postfix[i]], postfix[0: i] + postfix[i + 1:], n, res)

    def format(self, prefix):
        items = []
        for i in prefix:
            item = ""
            for j in range(len(prefix)):
                if j == i:
                    item += "Q"
                else:
                    item += "."
            items.append(item)
        return items

    def legal(self, l):
        length = len(l)
        if length <= 1:
            return True
        for i in range(length-1):
            if abs(l[length-i-2] - l[-1]) == i+1:
                return False
        else:
            return True


if __name__ == '__main__':
    Solution().solveNQueens(5)