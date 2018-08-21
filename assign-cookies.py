class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()

        if len(s) == 0:
            return 0

        count = 0
        for i in g:
            for j in xrange(len(s)):
                if i <= s[j]:
                    count += 1
                    s = s[j+1:]
                    break

        return count


if __name__ == '__main__':
    print Solution().findContentChildren([1, 2], [1, 2, 3])
    print Solution().findContentChildren([1, 2, 3], [3])