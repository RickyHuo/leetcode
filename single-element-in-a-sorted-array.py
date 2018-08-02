class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        while True:
            start = 0
            end = len(nums)
            index = (start + end) / 2
            if index == 1:
                if nums[index - 1] == nums[index]:
                    return nums[index + 1]
                else:
                    return nums[index - 1]

            if nums[index + 1] == nums[index]:
                if (index - start) % 2 == 0:
                    nums = nums[index:]
                else:
                    nums = nums[:index]
            elif nums[index] == nums[index - 1]:
                if (index + 1) % 2 == 0:
                    nums = nums[index+1:]
                else:
                    nums = nums[:index]
            else:
                return nums[index]


if __name__ == '__main__':
    print Solution().singleNonDuplicate([1,1,3,3,4,5,5])
    # print Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
