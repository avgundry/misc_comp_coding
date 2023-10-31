# doing this to practice for russian doll envelopes.

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        DP suboptimal solution
        """
        n = len(nums)

        if n == 0:
            return 0
        elif n == 1:
            return 1
        # dp[i] represents the smallest element that ends a subsequence of length i
        # i.e. in [3, 1, 2], we have that dp = [-1, 1, 2]; dp[0] is always -1
        dp = [float('inf')] * (n+1)
        dp[0] = -float('inf')

        for i in range(n):
            # binary search the range [0, i) for ind of largest number < nums[i]
            j = self.binarySearchGreater(dp, nums[i]) 
            if dp[j - 1] < nums[i] and nums[i] < dp[j]:
                dp[j] = nums[i]
        print(nums)
        print(dp)



        for k in range(len(dp) - 1, -1, -1):
            if dp[k] < float('inf'):
                return k

        return 1

    # return index of smallest num >= target
    def binarySearchGreater(self, nums, target):
        n = len(nums)
        left = 0
        right = n 

        while left < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        # if left < n and nums[left] < target:
        #     left += 1
            

        return left


        """
        Brute Force
        """
        # brute force method is to go through ALL subsequences
        # print(nums)
        # LIS = [1] * len(nums)

        # for i in range(len(nums) - 1, - 1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[i]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])

            

        # return max(LIS)


        


if __name__ == "__main__":
    s = Solution()
    print([1,3,5][s.binarySearchGreater([1, 3, 5], 4)])
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))