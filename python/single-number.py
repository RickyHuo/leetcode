class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        for i in range(length):
            index = i*2
            if index + 1 >= length:
                return nums[index]
            elif nums[index] != nums[index+1]:
                return nums[index]

    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
            print res
        return res


if __name__ == '__main__':
    print Solution().singleNumber([2,1,2])
    print Solution().singleNumber([4,1,2,1,2])
    print Solution().singleNumber_1([2,2,4,3,4])