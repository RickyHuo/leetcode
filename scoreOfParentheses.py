class Solution(object):

    @staticmethod
    def score_of_parentheses(s):
        """
        :type s: str
        :rtype: int
        """

        result = 0
        s = s.replace("()", " 1 ")
        s = s.replace("( 1 )", " 2 ")

        if s[0] == '(':

            s = s[1:-1]
            items = s.split(" ")

            for i in items:
                if i != "":
                    result += int(i)

            return result * 2
        else:
            items = s.split(" ")

            for i in items:
                if i != "":
                    result += int(i)
            return result

    @staticmethod
    def score_of_parentheses_1(s):
        lengths = []
        items = []
        s = s.replace("()", "1")
        print(s)
        for i in s:
            if i == '(':
                items.append(1)
                # lengths.append(len(items))
            elif i == ')':
                items.pop()
            lengths.append(len(items))

        # for i lengths

        print lengths


if __name__ == '__main__':
    Solution.score_of_parentheses_1("(()()((())))()")
