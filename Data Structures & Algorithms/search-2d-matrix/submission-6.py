class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1

        while (l <= r):
            print(f"l: {l}, r: {r}")
            mid_idx = (l + r) // 2
            row, col = divmod(mid_idx, n)
            matrix_val = matrix[row][col]
            print(f"target: {target} <=> matrix[{row}][{col}]: {matrix_val}")

            if (target < matrix_val):
                r = mid_idx - 1
            elif(target > matrix_val):
                l = mid_idx + 1
            else:
                return True 
        return False
        