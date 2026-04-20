class Solution:

    def dfs(self, grid: List[List[str]], row, col):
        if (row < 0) or (col < 0) or (row >= len(grid)) or (col >= len(grid[0]) or grid[row][col] == 0):
            return 0

        temp = grid[row][col]
        grid[row][col] = 0

        area_covered = self.dfs(grid, row + 1, col) + self.dfs(grid, row - 1, col) + self.dfs(grid, row, col + 1) + self.dfs(grid, row, col - 1)

        grid[row][col] = temp
        return area_covered + 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for row in range(len(grid)):
            for row_col in range(len(grid[0])):
                if grid[row][row_col] == 1:
                    print(max_area)
                    max_area = max(max_area, self.dfs(grid, row, row_col))

        return max_area