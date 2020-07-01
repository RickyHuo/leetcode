class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def helper(prefix, remain):
            length = len(remain)
            if length == 1:
                res.append(prefix + remain)
            else:
                for i in xrange(length):
                    helper(prefix + [remain[i]], remain[0:i] + remain[i+1:])

        helper([], nums)
        return res


if __name__ == '__main__':
    print Solution().permute([1, 2, 3, 4])

