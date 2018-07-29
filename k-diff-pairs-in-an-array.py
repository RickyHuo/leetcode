class Solution(object):
    @staticmethod
    def find_pairs(nums, k):
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

                if v in items.keys():
                    if items[v] == 1:
                        res += 1
                        items[v] -= 1

            return res


if __name__ == '__main__':
    print Solution.find_pairs([1, 3, 1, 5, 4], 1)
    print Solution.find_pairs([1, 3, 1, 5, 4], 0)
    print Solution.find_pairs([1, 2, 3, 4, 5], -1)
