from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # I honestly don't see how DP helps here...?
        return self.recurse(s, wordDict, 0)

    def recurse(self, s, wordDict, ind):
        if ind == len(s):
            # at end of word so were successful
            return True
        ret = False
        for word in wordDict:
            l = len(word)
            slice = s[ind: ind + l]
            if l + ind <= len(s) and word == s[ind:ind + l]:
                ret = ret or self.recurse(s, wordDict, ind + l)

        return ret 

if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
    print(s.wordBreak("cars", ["car","ca","rs"]))
        