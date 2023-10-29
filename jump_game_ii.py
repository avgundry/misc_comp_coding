from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        O(n) time solution; 
        optimization of DP approach
        """

        # in the DP approach we end up looking for the best number to jump
        # to many times (i.e. nums[i] time for each ith number).
        # instead we can work *forwards*, and keep track of the maximum
        # reachable space in 2 jumps from the current number
        n = len(nums)
        i = 0
        farthest = 0
        prev_pos = 0
        jumps = 0

        while (prev_pos < n - 1):
            # if we can jump farther from this number than all previous
            # numbers, then update it.
            farthest = max(farthest, i + nums[i])
            if i == prev_pos:
                # we've iterated to the end of all numbers reachable
                # by our previous farthest step
                # jump to the best position we've found so far.
                prev_pos = farthest
                jumps += 1
            i += 1

        return jumps

        """
        Bottom-up DP approach
        """
    #     dp = [float('inf')] * len(nums)
    #     return self.recurseJump(nums, 0, dp)

    # def recurseJump(self, nums, ind, dp):
    #     # break down into solving for min jumps from nums[i] to end.
    #     # to do so, work backwards to build dp
    #     dp[-1] = 0
    #     # for each of n numbers
    #     # must search through up to n numbers to build
    #     # so O(n^2) time. 
    #     for i in range(len(nums) - 2, -1, -1):
    #         min_num = float('inf')
    #         for j in range(i + 1, min(i + nums[i] + 1, len(nums))): 
    #             min_num = min(min_num, dp[j])
    #         dp[i] = min_num + 1

    #     return dp[ind]


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