class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        items = s.split(" ")

        res = ""
        for item in items:
            length = len(item)
            for i in range(length):
                res += item[length - i - 1]

            res += " "
        return res[:-1]

    def reverseWords_1(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
        items = []

        for i in s:
            if i != " ":
                items.append(i)
            else:
                while len(items) > 0:
                    res += items.pop()
                res += " "

        while len(items) > 0:
            res += items.pop()

        return res


if __name__ == '__main__':
    print Solution().reverseWords("Let's take LeetCode contest") + "d"
    print Solution().reverseWords_1("Let's take LeetCode contest") + "d"
