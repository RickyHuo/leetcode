class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = sum(nums)
        left = 0

        for i in xrange(len(nums)):
            if i == 0:
                right -= nums[i]
            else:
                right -= nums[i]
                left += nums[i-1]
            if left == right:
                return i
        return -1


if __name__ == '__main__':
    print Solution().pivotIndex([0])
    print Solution().pivotIndex([1, 2, 3])
    print Solution().pivotIndex([1, 7, 3, 6, 5, 6])