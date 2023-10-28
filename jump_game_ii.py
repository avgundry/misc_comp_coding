from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Bottom-up DP approach
        """
        dp = [float('inf')] * len(nums)
        return self.recurseJump(nums, 0, dp)

    def recurseJump(self, nums, ind, dp):
        # break down into solving for min jumps from nums[i] to end.
        # to do so, work backwards to build dp
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            # hmmm..is this the right way to do it?
            mins = [dp[x] for x in range(i, min(i + nums[i], len(nums)))]
            if mins:
                dp[i] = min(mins) + 1
            else:
                dp[i] = float('inf')
        print(dp)
        print(nums)

        return dp[ind]


    """
    Top-down DP approach
    """
    #     dp = [-1] * len(nums)
    #     return self.recurseJump(nums, 0, dp)

    # # break down into solving for nums[i:]
    # def recurseJump(self, nums, ind, dp):
    #     # base case
    #     if ind >= len(nums):
    #         return float('inf')
    #     elif dp[ind] != -1:
    #         return dp[ind]
    #     elif ind == len(nums) - 1:
    #         return 0
    #     mins = []

    #     for i in range(ind + 1, ind+nums[ind] + 1):
    #         mins.append(1 + self.recurseJump(nums, i, dp))

    #     if mins:
    #         dp[ind] = min(mins)
    #     else:
    #         dp[ind] = float('inf')

    #     return dp[ind]

    """
    Brute force recursion approach
    """ 

    #    return self.recurseJump(nums, 0)

    # # break down into solving for nums[i:]
    # def recurseJump(self, nums, ind):
    #     # base case
    #     if ind >= len(nums):
    #         return float('inf')
    #     elif ind == len(nums) - 1:
    #         return 0
    #     mins = []

    #     for i in range(ind + 1, ind+nums[ind] + 1):
    #         mins.append(1 + self.recurseJump(nums, i))

    #     return min(mins)
    
if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,3,1,1,4]))
    print(s.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))