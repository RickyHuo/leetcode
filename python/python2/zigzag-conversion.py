class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        items = []
        res = []
        for i in range(numRows):
            items.append([])

        index = 0
        while len(s) > 0:
            for i in range(numRows):
                if index % (numRows-1) == 0:
                    items[i].append(s[0])
                    s = s[1:]
                elif (i + index) % (numRows-1) == 0:
                    items[i].append(s[0])
                    s = s[1:]
                else:
                    items[i].append("")
                if len(s) == 0:
                    for j in range(numRows):
                        # print " ".join(items[j])
                        res.append("".join(items[j]))

                    return ''.join(res)
            index += 1


if __name__ == '__main__':
    print Solution().convert("ABc", 2)
