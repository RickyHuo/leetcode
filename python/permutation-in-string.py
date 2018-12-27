class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length = len(s1)
        dic1 = self.makeDic(s1)
        dic2 = self.makeDic(s2[: length])

        if dic1 == dic2:
            return True
        # print dic2
        for i in xrange(length, len(s2)):

            if s2[i] in dic2.keys():
                dic2[s2[i]] += 1
            else:
                dic2[s2[i]] = 1
            dic2[s2[i-length]] -= 1
            if dic2[s2[i-length]] == 0:
                del dic2[s2[i-length]]

            # print s2[i]
            # print dic2
            if dic1 == dic2:
                return True

        return False

    def makeDic(self, s):
        items = {}
        for i in s:
            if i in set(items.keys()):
                items[i] += 1
            else:
                items[i] = 1

        return items


if __name__ == '__main__':
    print Solution().checkInclusion("a", "ab")
    # print Solution().checkInclusion("hello", "ooolleoooleh")
    # print Solution().checkInclusion("ab", "eidbaooo")
    # print Solution().checkInclusion("ab", "eidboaoo")
