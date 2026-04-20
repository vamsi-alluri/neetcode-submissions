class Solution:

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def dfs(self, grid: List[List[str]], row, col):
        if (row < 0) or (col < 0) or (row >= len(grid)) or (col >= len(grid[0]) or grid[row][col] == 0):
            return 0

        grid[row][col] = 0

        area_covered = self.dfs(grid, row + 1, col) + self.dfs(grid, row - 1, col) + self.dfs(grid, row, col + 1) + self.dfs(grid, row, col - 1)

        return area_covered + 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for row in range(len(grid)):
            for row_col in range(len(grid[0])):
                if grid[row][row_col] == 1:
                    max_area = max(max_area, self.dfs(grid, row, row_col))

        return max_area