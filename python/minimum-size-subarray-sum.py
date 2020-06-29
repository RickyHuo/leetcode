class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:

        length = len(nums)
        flag = length + 1
        start, end = 0, 1

        while True:
            sum_r = sum(nums[start:end])
            if sum_r >= s:
                flag = min(flag, end - start)
                start += 1
            else:
                end += 1

            if end > length or start >= end:
                break

        if flag > length:
            return 0
        return flag


if __name__ == '__main__':
    print(Solution().minSubArrayLen(7, [2, 2, 2, 2]))
