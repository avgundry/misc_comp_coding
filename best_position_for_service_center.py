from typing import List

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # This is an optimization problem:
        # min sum_{i=0}^{n-1}sqrt[(x_ctr - x_i)^2 + (y_ctr - y_i)^2],
        # constraints: 1 <= len(positions) <= 50
        # apparently can also be thought of as finding the geometric median of 2D points.
        # Hm.
        n = len(positions)
        step_size = 1
        curr = [50, 50]
        # Set initial step size to 5, since we know 0 <= x, y <= 100.
        prev = [float('inf'), float('inf')]
        # curr = float('inf')

        while abs(self.euclideanDist(curr, prev)) > 10**(-5):
            grad_x, grad_y = self.getDistances(positions, curr[0], curr[1])
            prev = curr
            curr = [curr[0] - step_size * grad_x, curr[1] - step_size * grad_y]
            step_size *= 0.8
            # x_k, y_k = x_k - grad_x / dist, y_k - grad_y / dist

        return self.euclideanDist(curr, [0, 0])


    def getDistances(self, positions, x, y):
        # returns gradient distance x, y, then total distance
        grad_x = 0
        grad_y = 0
        for x_i, y_i in positions:
            denom = self.euclideanDist([x, y], [x_i, y_i])
            grad_x += (x - x_i) / denom
            grad_y += (y - y_i) / denom
        return grad_x, grad_y

    def euclideanDist(self, pos1, pos2):
        x, y = pos1
        x_i, y_i = pos2
        return ((x - x_i)**2 + (y - y_i)**2)**(1/2)

if __name__ == "__main__":
    s = Solution()
    print(s.getMinDistSum([[0, 1], [1, 0], [1, 2], [2, 1]]))
    print(s.getMinDistSum([[1, 1], [3, 3]]))

