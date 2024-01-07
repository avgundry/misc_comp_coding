import collections
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        # If we sort the nums, and then hash the count of each, this
        # effectively becomes the house robber problem.
        nums.sort()
        c = collections.Counter(nums)

        newnums = list(c)
        houses = []
        houses.append(newnums[0] * c[newnums[0]])
        for i in range(1, len(newnums)):
            if newnums[i] - 1 != newnums[i - 1]:
                houses.append(0)
            houses.append(newnums[i] * c[newnums[i]])


        # then optimize to get O(1) memory in this section
        prev = houses[0]
        curr = max(houses[0], houses[1])
        for i in range(2, len(houses)):
            prev, curr = curr, max(houses[i] + prev, curr)

        return curr


        # dp = [0 for _ in range(len(houses))]
        # dp[0] = houses[0]
        # dp[1] = max(houses[0], houses[1])
        # for i in range(2, len(houses)):
        #     dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])

        # return dp[-1]


        # I'm overthinking this.
        # Let dp[i] represent the max points gainable in subarray 
        # nums[:i + 1]. We have it in the format 
        # (largest # last added, total points at this index)
        # to easily check whether we can add to this for the next index
        # dp = [0 for _ in range(n)]
        # dp[0] = (nums[0], nums[0] * c[nums[0]])

        # # At each step, if nums[i] - 1 != nums[i - 1], simply add nums[i]
        # # to the max gainable.
        # for i in range(n):
        #     curr = nums[i]
        #     # Hmmm...in this case we COULD have that it's larger if
        #     # we add nums[i - 1] even though it wasn't included...
        #     if curr - 1 != nums[i - 1]:
        #         dp[i] = (nums[i], dp[i - 1] + nums[i]*c[nums[i]])
        #     else:
        #         if nums[i] * c[nums[i]] + dp
        #         dp[i] = max(nums[i], dp[i - 2] + nums[])

        

if __name__ == "__main__":
    s = Solution()
    print(s.deleteAndEarn([3, 4, 2]))
    print(s.deleteAndEarn([2,2,3,3,3,4]))




        