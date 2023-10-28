from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        O(1) memory approach
        """
        # represents index of last num to be True
        # starts at the end since that's what we hope to reach
        if len(nums) == 0 or len(nums) == 1:
            return True
        prev = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # start with the second-to-last num
            if nums[i] >= (prev - i):
                prev = i

        return prev == True

        """
        Bottom-up DP approach
        """ 
        # # can be optimized further - we don't even need this array.
        # dp = [-1] * len(nums)
        # dp[-1] = True
        # # represents index of last num to be True
        # # starts at the end since that's what we hope to reach
        # prev = len(nums) - 1
        # for i in range(len(nums) - 2, -1, -1):
        #     # start with the second-to-last num
        #     if nums[i] >= (prev - i):
        #         dp[i] = True
        #         prev = i
        #     else:
        #         dp[i] = False

        return dp[0]







    """
    Memoized recursive method
    """
    #     # memoize the brute force method to optimize.
    #     dp = [-1] * len(nums)
    #     return self.recurseJump(nums, 0, dp)

    # def recurseJump(self, nums, i, dp):
    #     # base cases
    #     if i > len(nums):
    #         return False
    #     elif dp[i] != -1:
    #         return dp[i]
    #     elif i == len(nums) - 1:
    #         dp[i] = True
    #         return True

    #     reached = False
    #     for j in range(1, nums[i] + 1):
    #         reached = reached or self.recurseJump(nums, i + j, dp)

    #     return reached
        
    


    """
    Brute force recursive method
    """
    #     # each time, can jump up to nums[i] spaces, where i is current index

    #     # can recursively return whether or not we can reach the last index.
    #     # optimize out of recursion afterwards.

    #     # start at first index
    #     return self.recurseJump(nums, 0)

    # def recurseJump(self, nums, i):
    #     # base cases.
    #     if i >= len(nums):
    #         return False
    #     elif i == len(nums) - 1:
    #         return True

    #     curr = nums[i]
    #     reached = False
    #     for j in range(1, curr + 1):
    #         reached = reached or self.recurseJump(nums, i + j)
        
    #     return reached

if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))