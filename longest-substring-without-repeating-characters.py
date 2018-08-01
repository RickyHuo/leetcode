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
                nums = max(nums, length)
                index = items.index(i)
                items = items[index + 1:]

            items.append(i)

        nums = max(len(items), nums)

        return nums


if __name__ == '__main__':
    # print Solution().lengthOfLongestSubstring('b')
    # print Solution().lengthOfLongestSubstring('')
    # print Solution().lengthOfLongestSubstring('au')
    print Solution().lengthOfLongestSubstring('abcadcbb')
    print Solution().lengthOfLongestSubstring('pwwkew')
    print Solution().lengthOfLongestSubstring('dvdf')
