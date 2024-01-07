from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        dist = lambda c1, c2: ((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)**(1/2)

        """
        I see - we aren't returning a tower coordinate necessarily.
        Brute force method is create a giant matrix of integer coordinates;
        each coordinate will be within [0, max_x] * [0, max_y].
        """
        max_x = max(towers, key=lambda x: x[0])[0]
        max_y = max(towers, key=lambda x: x[1])[1]
        # All qualities in all coordinates are 0 to start.
        qualities = [[0 for _ in max_x] for _ in max_y]

        # then - and this is truly horrible runtime - we loop through every
        # tower and adds its quality to all reachable coordinates.
        # god this would take too long. ughhhh
        for tower in towers:


        # qualities = []
        # for i in range(len(towers)):
        #     curr = towers[i]
        #     qual = 0
        #     for j in range(len(towers)):
        #         d = dist(curr, towers[j])
        #         if d < radius:
        #             qual += towers[j][2] // (1 + d)
        #     qualities.append([curr[0], curr[1], qual])

        # print(qualities)
        # best = max(qualities, key=lambda x: (x[2], -x[0], -x[1]))
        # return [best[0], best[1]]


if __name__ == "__main__":
    s = Solution()
    print(s.bestCoordinate([[1,2,5],[2,1,7],[3,1,9]], 2))
    print(s.bestCoordinate([[2,1,9],[0,1,9]], 2))