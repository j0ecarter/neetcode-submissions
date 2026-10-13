class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            row = mid // COLS
            col = mid % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False