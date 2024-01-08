from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        paths = []
        l1 = len(grid)
        l2 = len(grid[0])

        if l1 < 1 or l2 < 1:
            return 0

        """Bottom-up DP"""
        # Let dp[i][j] represent the minimum path sum to get to 
        # position[i][j], *including* count of grid[i][j] itself.
        dp = [[-1 for _ in range(l2)] for _ in range(l1)]
        dp[0][0] = grid[0][0]
        for i in range(l1):
            for j in range(l2):
                if i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0 and i != 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                elif j != 0 and i != 0:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

        """Brute force recursion"""
    #     self.recurse(grid, paths, 0, 0, 0)
    #     return min(paths)

    # def recurse(self, grid, paths, m, n, total):
    #     l1 = len(grid)
    #     l2 = len(grid[0])
    #     if m == l1 - 1 and n == l2 - 1:
    #         paths.append(total + grid[m][n])
    #         return
    #     # if m >= l or n >= len(grid[0]):
    #     #     # at the end
    #     #     # paths.append(total)
    #     #     return
    #     elif m == l1 - 1:
    #         # can only move right, not down
    #         self.recurse(grid, paths, m, n + 1, total + grid[m][n])
    #     elif n == l2 - 1:
    #         self.recurse(grid, paths, m + 1, n, total + grid[m][n])
    #     else:
    #         self.recurse(grid, paths, m, n + 1, total + grid[m][n])
    #         self.recurse(grid, paths, m + 1, n, total + grid[m][n])

              
        

if __name__ == "__main__":
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))