from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        # O(nlog(n)) time
        envelopes.sort()
        # maaaybe DP is 2d here. and dp[x][y] = best possible at a given x,y.
        # then when we solve for...hmm. well that could get HUGE very easily
        # dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp = n * [-1]
        dp[0] = 1
        longest = max(max(envelopes))
        print("LONGEST")
        print(longest)

        # as it stands this is O(n^2).
        # Is there a way to bring it down to O(nlog(n)), or even O(n)?
        # the sorting would still eclipse it in the latter case but...hm.
        # maybe looking forward every time, like longest subsequence or...
        # something. So for env[1] we find the next one it fits in...fuck no
        # that's still O(n^2). Shit.
        # maybe do a 2d coordinate matrix...but the memory would be HUGE.
        # like if it's a 10k by 10k envelope it'd be a 10000^2 matrix. nope...
        # no removing some doesn't work. urgh.
        # I suppose let's try the 2D matrix...

        


        # for i in range(1, len(envelopes)):
        #     curr = envelopes[i]
        #     # find the largest envelope preceding it that it can hold
        #     found = False
        #     mxs = [dp[j] for j in range(i) if envelopes[j][0] < curr[0] and envelopes[j][1] < curr[1]]
        #     if mxs:
        #         dp[i] = max(mxs) + 1
        #     else:
        #         dp[i] = 1

        # return max(dp)
        


        # dp = n * [-1]

        # # let dp[i] be [max envelopes in envelopes[:i], index of best choice]
        # dp[0] = 1
        
        # # do we sort them first...?
        # envelopes.sort(key=lambda x:(x[0], x[1]))
        # print(envelopes)

        
        # return self.recurseEnv(envelopes, 0, dp)


            
    # def recurseEnv(self, envelopes, ind, dp):
    #     # base case
    #     if ind == len(envelopes):
    #         return max(dp)
    #     mx = 1

    #     curr = envelopes[ind]
    #     for i in range(ind):
    #         other = envelopes[i]
    #         if other[0] < curr[0] and other[1] < curr[1]:
    #             mx = max(mx, dp[i] + 1)
    #     dp[ind] = mx
    #     return self.recurseEnv(envelopes, ind + 1, dp)


if __name__ == "__main__":
    s = Solution()
    print(s.maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]))
    print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
    print(s.maxEnvelopes([[1,1],[1,1],[1,1]]))