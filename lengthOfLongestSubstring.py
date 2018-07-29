class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        nums = 0
        items = []
        for i in s:
            if i in items:
                length = len(items)
                if length > nums:
                    nums = length
                index = items[::-1].index(i)
                items = items[(length - index):]

            items.append(i)

        if len(items) > nums:
            return len(items)

        return nums


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring('b')
    print Solution().lengthOfLongestSubstring('')
    print Solution().lengthOfLongestSubstring('au')
    print Solution().lengthOfLongestSubstring('abcabcbb')
    print Solution().lengthOfLongestSubstring('pwwkew')
    print Solution().lengthOfLongestSubstring('dvdf')