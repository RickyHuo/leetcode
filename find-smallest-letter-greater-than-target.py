class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        max_item = max(letters)
        min_item = min(letters)

        if max_item <= target:
            return min_item

        elif min_item > target:
            return min_item

        else:
            for i in letters:
                if i > target:
                    return i


if __name__ == '__main__':
    print Solution().nextGreatestLetter(["c", "f", "j"], "a")
    print Solution().nextGreatestLetter(["c", "f", "j"], "c")
    print Solution().nextGreatestLetter(["c", "f", "j"], "d")
    print Solution().nextGreatestLetter(["c", "f", "j"], "g")
    print Solution().nextGreatestLetter(["c", "f", "j"], "j")
    print Solution().nextGreatestLetter(["c", "f", "j"], "k")
