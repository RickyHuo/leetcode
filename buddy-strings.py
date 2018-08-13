class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        length = len(A)
        items = []

        if length != len(B):
            return False

        for i in xrange(length):
            if A[i] != B[i]:
                items.append(i)

        if len(items) == 0:
            for i in A:
                if A.count(i) >= 2:
                    return True
            return False
        elif len(items) != 2:
            return False
        else:
            if A[items[0]] == B[items[1]] and A[items[1]] == B[items[0]]:
                return True
            else:
                return False


if __name__ == '__main__':
    print Solution().buddyStrings("ab", "ba")
    print Solution().buddyStrings("aaaaaaabc", "aaaaaaacb")
    print Solution().buddyStrings("aa", "aa")
    print Solution().buddyStrings("ab", "ab")
    print Solution().buddyStrings("ab", "ca")