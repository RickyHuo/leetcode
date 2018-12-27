class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        items = {}
        for i in S:
            if i in items:
                items[i] += 1
            else:
                items[i] = 1

        res = 0
        for i in J:
            if i in items:
                res += items[i]

        return res


if __name__ == '__main__':
    print Solution().numJewelsInStones("aA", "aAAbbbb")
    print Solution().numJewelsInStones("z", "ZZ")
