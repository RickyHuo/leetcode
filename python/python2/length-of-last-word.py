class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in s[::-1]:
            if res == 0 and i == ' ':
                continue
            elif i != ' ':
                res += 1
            else:
                break
        return res


if __name__ == '__main__':
    print Solution().lengthOfLastWord("f ")
