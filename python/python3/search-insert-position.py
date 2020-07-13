class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            index = (begin + end) // 2
            if begin == index:
                return begin

            val = nums[index]
            if val == target:
                return index
            elif val > target:
                end = index - 1
            else:
                begin = index + 1
        return begin


if __name__ == '__main__':
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    print(Solution().searchInsert([1, 3, 5, 6], 1))
    print(Solution().searchInsert([1, 3, 5, 6], 0))
