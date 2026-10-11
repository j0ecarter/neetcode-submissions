class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                sq_index = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in squares[sq_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[sq_index].add(val)

        return True