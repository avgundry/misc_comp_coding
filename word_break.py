from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None for _ in range(len(s))]
        self.recurse(s, wordDict, len(s) - 1, dp)
        return dp[0]

    def recurse(self, s, wordDict, ind, dp):
        if ind == 0:
            # at end of word so were successful
            dp[0] == True
        elif dp[ind] != None:
            return dp[ind]
        else:
            for word in wordDict:
                l = len(word)
                # slice = s[ind - l: ind]
                if ind - l >= 0 and word == s[ind - l:ind]:
                    dp[ind] = True
                    return self.recurse(s, wordDict, ind + l)
            dp[ind] = False or dp[ind]

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
        