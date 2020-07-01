class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == list(set(nums)):
            return False
        else:
            return True


if __name__ == '__main__':
    print Solution().containsDuplicate([1, 2, 3, 4, 1])
