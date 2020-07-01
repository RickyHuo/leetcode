class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        items = {}
        res = []

        for i in A.split(" ") + B.split(" "):
            if items.has_key(i):
                items[i] += 1
            else:
                items[i] = 1

        for i in items:
            if items[i] == 1:
                res.append(i)

        return res


if __name__ == '__main__':
    print Solution().uncommonFromSentences("apple apple", "banaba")