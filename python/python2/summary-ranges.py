class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tag = 0
        index = 0
        items = []
        for i in xrange(len(nums)):
            if nums[i] != tag:
                tag = nums[i]+1
                items.append(nums[index:i])
                index = i
            else:
                tag += 1

        items.append(nums[index:])
        return self.generate_res(items)

    def generate_res(self, items):
        res = []
        for i in items:
            if len(i) == 0:
                pass
            elif len(i) == 1:
                res.append(str(i[0]))
            else:
                res.append("{}->{}".format(i[0], i[-1]))

        return res


if __name__ == '__main__':
    print Solution().summaryRanges([2,3,4,6,8,9])
