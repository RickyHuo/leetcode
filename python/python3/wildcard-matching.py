class Solution:

    @staticmethod
    def duplicate(str):
        for i in range(1, len(str))[::-1]:
            if str[i] == '*' and str[i-1] == '*':
                str = str[0:i] + str[i + 1:]
        return str

    def isMatch(self, s: str, p: str) -> bool:
        m, n = 0, 0

        p = self.duplicate(p)
        len1 = len(s)
        len2 = len(p)

        while m < len1 and n < len2:
            if p[n] == "?":
                return self.isMatch(s[m + 1:], p[n + 1:])
            elif p[n] == "*":
                if n == len2 - 1:
                    return True

                for i in range(len1 - m + 1):
                    if self.isMatch(s[m + i:], p[n + 1:]):
                        return True
                return False

            else:
                if s[m] != p[n]:
                    return False
                else:
                    m += 1
                    n += 1
        if m == len1:
            if n == len2:
                return True
            elif p[n:].count("*") == len2 - n:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    print(Solution().isMatch("abcde", "ab?d"))
    print(Solution().isMatch("abcdefg", "a?g"))
    print(Solution().isMatch("adceb", "*a*b"))
    print(Solution().isMatch("abc", "a*****"))
    print(Solution().isMatch("abc", "a**?"))
    print(Solution().isMatch("abc", "a**d"))
    print(Solution().isMatch("abc", "a**d"))
    print(Solution().isMatch("", "*"))
    print(Solution.duplicate("****a"))
    print(Solution.duplicate("****a***"))

