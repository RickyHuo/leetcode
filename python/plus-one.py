class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits = [str(i) for i in digits]
        num = int(''.join(digits)) + 1
        return [int(i) for i in str(num)]


if __name__ == '__main__':
    print Solution().plusOne([1, 2, 3])
