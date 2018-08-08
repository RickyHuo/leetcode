class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)

        for i in range(length / 2):
            res = length % (i + 1)
            if res == 0:
                if s[0:i+1] * (length / (i + 1)) == s:
                    return True

        return False


if __name__ == '__main__':
    print Solution().repeatedSubstringPattern("aba")
    print Solution().repeatedSubstringPattern("abcabcabcabc")