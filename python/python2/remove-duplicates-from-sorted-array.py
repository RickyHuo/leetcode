class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        flag = 1
        for i in xrange(1, len(nums)):
            if nums[i] == nums[j]:
                pass
            else:
                j = i
                flag += 1
        return flag


if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1, 2])
