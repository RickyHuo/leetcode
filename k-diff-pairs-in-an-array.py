class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 0:
            return 0

        elif k == 0:
            items = {}
            for i in nums:
                if nums.count(i) - 1 > 0:
                    items[i] = 0

            return len(items)

        else:
            items = {}
            res = 0
            for i in nums:
                items[i] = 1

            for i in nums:
                v = i+k
                try:
                    val = items[v]
                    res += 1
                    del items[v]
                except Exception as e:
                    pass

            return res


if __name__ == '__main__':
    print Solution().findPairs([1, 3, 1, 5, 4], 1)
    print Solution().findPairs([1, 3, 1, 5, 4], 0)
    print Solution().findPairs([1, 2, 3, 4, 5], -1)
