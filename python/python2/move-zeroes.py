class Solution(object):
    @staticmethod
    def move_zeroes_1(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        indexs = []
        for i in range(len(nums)):
            if nums[i] == 0:
                indexs.append(i)

        for i in reversed(indexs):
            del nums[i]

        for i in range(len(indexs)):
            nums.append(0)

        return nums

    @staticmethod
    def move_zeroes_2(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(0, length):
            index = length - i - 1
            if nums[index] == 0:
                nums.append(0)
                nums.pop(index)

        print nums


if __name__ == '__main__':
    nums = Solution.move_zeroes_1([2, 0, 4, 3, 0, 3])
    nums = Solution.move_zeroes_2([0, 0, 0, 0, 0, 3])
    print nums
