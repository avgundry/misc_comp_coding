class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # This definitely seems like a DP problem. 
        # We can make a 2D DP array, where DP[i][j] represents whether
        # we can reach the point (i, j) from (low_x, low_y). Then just do a
        # bottom-up build of the array.

        # Unsure whether moving *both* points is permissible.
        if (sx < tx and sy > ty) or (sx > tx and sy < ty):
            return False

        low_x = min(sx, tx)
        high_x = max(sx, tx)
        low_y = min(sy, ty)
        high_y = max(sy, ty)

        # Hitting MLE errors...I suppose *one* way is to mod the higher
        # coordinate by the smaller ones...?
        # If we have (1, 2), (9, 1002)...can we mod (9, 1002) by 2, 1
        # respectively? No...not quite. 
        # Can this be converted to a 1D array?
        # We can try doing a top-down approach and seeing if that works
        # Wait - if we have coords (9, 1002) and (1002 - y1) % 9 == 0.
        # That means if we can get x1 to 9, we can repeatedly add it to y1
        # and thus know we can solve it.

        # Let False represent an unreachable point.
        # True represents a reachable point.
        dp = [[False for _ in range(high_y - low_y + 1)] for _ in range(high_x - low_x + 1)]
        dp[0][0] = True
        x_len = len(dp)
        y_len = len(dp[0])
        for i in range(x_len):
            for j in range(y_len):
                if dp[i][j]:
                    # The *adjusted* points - so e.g. sx 1, sy 1 would be grid 0 0.
                    # so we need to add those to it.
                    x = low_x + i 
                    y = low_y + j 
                    if i + y < x_len:
                        dp[i + y][j] = True
                    if j + x < y_len:
                        dp[i][j + x] = True
        # print(dp)
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print(s.reachingPoints(1, 1, 3, 5))