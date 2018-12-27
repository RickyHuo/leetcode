class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        items = [s[k * i: k * i + k] for i in range(len(s) / k + 1)]
        reverse_items = []
        for i in xrange(len(items)):
            if i % 2 == 0:
                reverse_items.append(items[i][::-1])
            else:
                reverse_items.append(items[i])
        return ''.join(reverse_items)


if __name__ == '__main__':
    print Solution().reverseStr('abcdefg', 3)
