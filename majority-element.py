# encoding: utf-8

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        items = {}
        length = len(nums)

        for i in nums:
            if i in items:
                items[i] += 1
            else:
                items[i] = 1

            if items[i] > (length / 2.0):
                return i


if __name__ == '__main__':
    print Solution().majorityElement([1,2,1,2,1])

    # https://blog.csdn.net/chfe007/article/details/42919017
    # 摩尔投票算法
