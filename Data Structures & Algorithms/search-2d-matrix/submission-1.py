class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        mid_idx_v = 0
        while(top <= bottom): # First, figure out the which row the target is in.
            mid_idx_v = (top + bottom) // 2
            
            if (top == bottom):
                mid_idx_h = 0
                while(left < right):    # Then, Search in the row it belongs.
                    print(f"l: {left}, r: {right}")
                    print("Considered array:", nums[left:right])
                    mid_idx_h = (left + right) // 2
                    print(f"target: {target} <=> matrix[{mid_idx_v}][{mid_idx_h}]: {matrix[mid_idx_v][mid_idx_h]}")

                    if (target < matrix[mid_idx_v][mid_idx_h]):
                        right = mid_idx_h - 1
                    elif (target > matrix[mid_idx_v][mid_idx_h]):
                        left = mid_idx_h + 1
                    else:
                        return True
            
            if (target < matrix[mid_idx_v][0]):
                bottom = mid_idx_v - 1
            elif (target > matrix[mid_idx_v][0]):
                top = mid_idx_v + 1
            else:
                return True
        return False
        