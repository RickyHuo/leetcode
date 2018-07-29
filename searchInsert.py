class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)

        while True:
            index = (start + end) / 2
            value = nums[index]

            if target == value:
                return index
            elif target > value:
                if end - start == 1:
                    return end
                else:
                    start = index
            elif target < value:
                if end - start == 1:
                    return start
                else:
                    end = index


if __name__ == '__main__':
    # 二分查找
    print Solution().searchInsert([1,3,5,6], 5)