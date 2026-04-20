class Solution:

    def dfs(self, grid: List[List[str]], row, col):
        if (row < 0) or (col < 0) or (row >= len(grid)) or (col >= len(grid[0]) or grid[row][col] == "0"):
            return

        grid[row][col] = "0"

        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
          
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        for row in range(len(grid)):
            for row_col in range(len(grid[0])):
                if grid[row][row_col] == "1":
                    print(grid)
                    self.dfs(grid, row, row_col)
                    num_islands += 1

        return num_islands

                
         