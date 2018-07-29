#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    @staticmethod
    def two_sum_1(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    @staticmethod
    def two_sum_2(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            v = target - nums[i]
            if v in nums:
                if i != nums.index(v):
                    return [i, nums.index(v)]


if __name__ == '__main__':

    '''
    疑问：
        方法二的速度为什么快于方法一？
        内置方法Index的实现原理是什么？
    '''
    nums = [2, 4, 8, 12]
    target = 12
    print Solution.two_sum_1(nums, target)
    print Solution.two_sum_2(nums, target)
