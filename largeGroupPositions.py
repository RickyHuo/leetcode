class Solution(object):

    @staticmethod
    def largeGroupPositions(S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        items = {}

        for i in range(len(S)):
            char = S[i]
            if char in items.keys():
                items[i]['nums'] += 1
            else:
                item = {
                    'nums': '1',
                    'index': i
                }
                items[char] = item

        print items


if __name__ == '__main__':
    print Solution.largeGroupPositions('abcdddeeeeaabbbcd')