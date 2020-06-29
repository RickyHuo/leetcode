class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:

        nums = nums.sort()
        return nums[-k]

    def quick_sort(self, nums):

        if len(nums) <= 1:
            return nums
        before = []
        after = []

        flag = nums[0]

        for i in range(len(nums) - 1):
            num = nums[i + 1]
            if num < flag:
                before.append(num)
            else:
                after.append(num)

        before = self.quick_sort(before)
        after = self.quick_sort(after)

        before.append(flag)
        before.extend(after)
        return before


if __name__ == '__main__':
    print(Solution().findKthLargest([4, 3, 2, 5], 2))
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(Solution().findKthLargest([3], 1))
