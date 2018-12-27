class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        length = len(S)
        index = []
        items = []
        for i in xrange(length):
            if S[i] == C:
                index.append(i)

        for i in xrange(length):
            print i, index
            if index[0] == i:
                items.append(0)
            elif len(index) == 1:
                items.append(abs(i - index[0]))
            elif index[0] < i < index[1]:
                items.append(min(i - index[0], index[1] - i))
            elif i < index[0]:
                items.append(index[0] - i)
            else:
                items.append(i - index[1])
                index.pop(0)

        return items


if __name__ == '__main__':
    print Solution().shortestToChar("adbafdafdafe", "e")