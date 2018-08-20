class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        for i in range(1, n+1):
            self.search([i], range(1, i) + range(i + 1, n+1), k, res)

        return res

    def search(self, prefix, postfix, n, res):
        # print prefix, postfix
        if len(prefix) == n:
            # print prefix
            res.append(prefix)
        else:
            for i in range(len(postfix)):
                if postfix[i] > prefix[-1]:
                    self.search(prefix + [postfix[i]], postfix[i + 1:], n, res)


if __name__ == '__main__':
    print Solution().combine(20, 16)