from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)

        if n == 0:
            return 0
        elif n == 1:
            return 1

        dp = [float('inf')] * (n + 1) 
        dp[0] = -float('inf')
        envelopes.sort(key=lambda x: (x[0], -x[1]))


        for _, height in envelopes:
            j = self.binarySearch(dp, height)
            if dp[j - 1] < height and height < dp[j]:
                dp[j] = height

        for k in range(len(dp) - 1, -1, -1):
            if dp[k] != float('inf'):
                return k
        
        return 1


    # return smallest number >= target
    def binarySearch(self, nums, target):
        n = len(nums)
        left = 0
        right = n

        while left < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    s = Solution()
    print(s.maxEnvelopes([[46,89],[50,53],[52,68],[72,45],[77,81]]))
    print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
    print(s.maxEnvelopes([[1,1],[1,1],[1,1]]))