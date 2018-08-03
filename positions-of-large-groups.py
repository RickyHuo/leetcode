class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        count = 0
        flag = S[0]
        index = 0
        items = []

        for i in xrange(len(S)):
            if S[i] != flag:
                if count >= 3:
                    items.append([index, index+count-1])

                index = i
                flag = S[i]
                count = 1
            else:
                count += 1

        if count >= 3:
            items.append([index, index + count - 1])

        return items


if __name__ == '__main__':
    print Solution().largeGroupPositions("aa")