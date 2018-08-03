class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        items = [0]
        length = len(nums)

        for i in xrange(length):
            if nums[i] == 0:
                items.append(i + 1)
        items.append(length + 1)

        max_c = 0

        for i in range(1, len(items)):
            max_c = max(max_c, items[i] - items[i - 1] - 1)

        return max_c


if __name__ == '__main__':
    print Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
