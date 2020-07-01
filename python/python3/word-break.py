class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        tmp = s
        length = len(s)
        max_l = 0
        for i in wordDict:
            max_l = max(max_l, len(i))
        for i, j in enumerate(s):
            tmp = tmp[:length-i]
            if len(tmp) > max_l:
                continue
            if tmp in wordDict:
                if tmp == s:
                    return True
                elif self.wordBreak(s[length-i:], wordDict):
                    return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreak("applepenapple", ["apple", "pen"]))
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(s.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
    print(s.wordBreak("aaaaaaa", ["aaaa", "aa"]))