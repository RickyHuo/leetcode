class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)

        while True:

            index = (start + end) / 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                if end == index:
                    return -1
                else:
                    end = index
            else:
                if start == index:
                    return -1
                else:
                    start = index


if __name__ == '__main__':
    print Solution().search([1,3], 2)
