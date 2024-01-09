from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            # could not catch any water.
            return 0

        left = 0
        lheight = height[left]
        total = 0
        curr_total = 0
        # O(n) time
        for i in range(1, n):
            if height[i] >= lheight:
                # found the new barrier
                lheight = height[i]
                left = i
                total += curr_total
                curr_total = 0
            else:
                curr_total += lheight - height[i]

        # This occurs if the last index was not a boundary point.
        # Thus we have to do the same procedure in reverse, and only up
        # to the previous boundary.
        # Also O(n) time; on average will be O(n/2)
        if left != n - 1:
            curr_total = 0
            right = n - 1
            rheight = height[right]
            for i in range(n - 1, left - 1, -1):
                if height[i] >= rheight:
                    rheight = height[i]
                    right = i
                    total += curr_total
                    curr_total = 0
                else:
                    curr_total += rheight - height[i]

        # Thus O(n) time, O(1) space.

        return total


if __name__ == "__main__":
    s = Solution()
    print(s.trap([1,0,1]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([4,2,0,3,2,5]))
    print(s.trap([4,2,3]))


