from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # My thinking on this is that there is at most 1 queen in each
        # row and in each column.
        # We may iterate over available spaces in each row.
        # We know that there will be no less than n queens. Given our
        # first constraint, we then must have that there is exactly 1
        # queen in each row and in each column.
        # In the case that there are 2 queens, there is no way to place
        # 2 on a 2x2 board. Thus we simply return.
        # if n == 2:
        #     return []

        # I believe we can begin by brute-force recursing through all
        # possible solutions. We will store each solution in an array
        # of grids.
        grids = []
        # First, we need to generate the grid they're on.
        # Let an empty string '' represent a space where we haven't
        # decided whether it should contain a queen or be empty.
        for j in range(n):
            grid = [['' for _ in range(n)] for _ in range(n)]
            self.recurseQueens(n, grids, grid.copy(), 0, j)
        return grids

    # i represents the current row.
    # j represents the current column.
    # (i, j) is where the queen will be placed.
    def recurseQueens(self, n, grids, grid, i, j):

        assert(grid[i][j] == '')
        # then iterate over each column position. As we do so, we can 
        # use the brute force method of forcing all spaces it would 
        # collide with to be empty. No need to check previous squares
        # since we're guaranteed previous rows will be already filled.
        for x in range(i, n):
            for y in range(n):
                # Fill the given coordinates with a queen.
                if x == i and y == j:
                    grid[x][y] = 'Q' 
                elif x == i:
                    # The same row must be empty.
                    grid[x][y] = '.'
                elif y == j:
                    # The same column must be empty.
                    grid[x][y] = '.'
                elif abs(y - j) == abs(x - i):
                    # Diagonals must be empty. 
                    # This occurs when we move the same amount in both
                    # the horizontal and vertical directions.
                    grid[x][y] = '.'

        # If we're at the last row, we're finished.
        if i >= n - 1:
            # Apparently, have to convert each row into a string.
            for z in range(n):
                grid[z] = ''.join(grid[z])
            grids.append([row[:] for row in grid])
            return


        # Otherwise, call it on each viable position in the next row.
        found = False
        for y in range(n):
            if grid[i + 1][y] != '.':
                self.recurseQueens(n, grids, [row[:] for row in grid], i + 1, y)
                found = True
        # If couldn't continue then break recursion
        if not found:
            # grids.append([])
            return 


if __name__ == "__main__":
    s = Solution()
    # print(s.solveNQueens(1))
    # print(s.solveNQueens(2))
    # print(s.solveNQueens(3))
    # print(s.solveNQueens(4))
    x = s.solveNQueens(5)
    for row in x:
        print(row)
        