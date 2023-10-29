from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # ok, utter brute force method.
        # make height into a 2d array of 0s and 1s.
        # find # of 0s between 1s on each level.
        # return the total num of 0s.
        highest = max(height)
        water = 0

        # walls[x][y] = 1 if wall, 0 if not
        walls = [[x < height[i] for i in range(len(height))] for x in range(highest)]
        # print(walls)
        # for each height level
        for h in range(highest):
            left = -1
            for j in range(len(walls[0])):
                if walls[h][j] == 1:
                    if left != -1:
                        water += j - left - 1
                    left = j

        return water
        # # for i in range(highest):
        # #     walls.append([x < height[i] for x in range(len(height))])

        # print(walls)



if __name__ == "__main__":
    s = Solution()
    print(s.trap([1,0,1]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


