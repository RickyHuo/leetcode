# encoding: utf-8


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 去重
        nums = list(set(nums))
        # 排序
        nums = sorted(nums)

        for i in xrange(len(nums)):
            if nums[i] > 0:
                nums = nums[i:]
                break

        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


if __name__ == '__main__':
    print Solution().firstMissingPositive([7, 8, 9, 11, 12])
    print Solution().firstMissingPositive([3, 4, -1, 1])
    print Solution().firstMissingPositive([0, 1, 1000])
    print Solution().firstMissingPositive([0, 2, 2, 1, 1])
