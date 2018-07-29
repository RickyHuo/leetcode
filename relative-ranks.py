class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        sort_nums = sorted(nums)[::-1]
        items = {}

        for i in xrange(len(sort_nums)):
            if i == 0:
                items[sort_nums[i]] = "Gold Medal"
            elif i == 1:
                items[sort_nums[i]] = "Silver Medal"
            elif i == 2:
                items[sort_nums[i]] = "Bronze Medal"
            else:
                items[sort_nums[i]] = str(i + 1)

        return [items[i] for i in nums]


if __name__ == '__main__':
    print Solution().findRelativeRanks([5, 4])