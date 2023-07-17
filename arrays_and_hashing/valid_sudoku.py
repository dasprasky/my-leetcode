# https://leetcode.com/problems/valid-sudoku/
from collections import defaultdict


class Solution:
    def valid_sudoku(self, board: list[list[str]]) -> bool: 
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if item == ".": 
                    continue
                if item in rows[r] or item in cols[c] or item in squares[r // 3, c // 3]: 
                    return False
                rows[r].add(item)
                cols[c].add(item)
                squares[r//3, c//3].add(item)

        return True
    
print(Solution().valid_sudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

# linear time and space complexity 
# O(9^2) 