from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        # Hmmm...god idk. Let dp[i] be the LIS up to index i???
        # Couldn't that conceivably miss some, though?


        """Brute force recursion method"""
    #     # First...how do we find a LIS to begin with.
    #     paths = []
    #     for i in range(len(nums)):
    #         self.recurse(nums, paths, [], i)
    #     total = 0
    #     paths.sort(key=lambda x: len(x), reverse=True)
    #     for path in paths:
    #         if len(path) == len(paths[0]):
    #             total += 1
    #         else:
    #             return total

    # def recurse(self, nums, paths, path, ind):
    #     if ind >= len(nums):
    #         paths.append(path)
    #     elif path and nums[ind] <= path[-1]:
    #         # print(path[-1])
    #         paths.append(path)
    #     else:
    #         for i in range(ind + 1, len(nums) + 1):
    #             self.recurse(nums, paths, path.copy() + [nums[ind]], i)

if __name__ == "__main__":
    s = Solution()
    print(s.findNumberOfLIS([1,3,5,4,7]))