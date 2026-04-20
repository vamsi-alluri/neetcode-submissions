class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        # Step 1: Find the correct row
        top, bottom = 0, m - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                # Target must be in this row
                break

        if not (top <= bottom):
            return False

        row = (top + bottom) // 2

        # Step 2: Binary search within that row
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True

        return False
