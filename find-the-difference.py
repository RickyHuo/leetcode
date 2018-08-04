class Solution(object):
    @staticmethod
    def find_the_difference(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        sort_s = sorted(s)
        sort_t = sorted(t)

        for i in range(len(sort_t)):

            if i + 1 > len(sort_s):
                return sort_t[i]

            if sort_t[i] != sort_s[i]:
                return sort_t[i]


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    print Solution.find_the_difference(s, t)
