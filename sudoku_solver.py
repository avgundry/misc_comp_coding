import collections
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

    def isValid(self, board):
        # Returns true if the given board is valid.

        # Length of the board
        m = 9
        # rowsets= [collections.Counter(row) for row in board]
        rowsets = [set() for _ in range(m)]
        colsets = [set() for _ in range(m)]
        boxsets = collections.defaultdict(lambda: collections.defaultdict(set))

        for i in range(m):
            for j in range(m):
                curr = board[i][j]
                if curr in rowsets[i] or curr in colsets[j] or \
                        curr in boxsets[i // 3][j // 3]:
                    return False
                rowsets[i].add(curr)
                colsets[j].add(curr)
                boxsets[i // 3][j // 3].add(curr)
        
        return True

    
