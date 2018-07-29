class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        nums_t = sorted(nums)
        if nums_t[-1] >= nums_t[-2] * 2:
            return nums.index(nums_t[-1])
        else:
            return -1


if __name__ == '__main__':
    print Solution().dominantIndex([1, 2, 3, 4])
