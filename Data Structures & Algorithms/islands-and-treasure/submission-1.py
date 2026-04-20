class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid or not grid[0]:
            return

        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int, dist: int):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            if grid[r][c] < dist:
                return
            # only update distance if smaller
            grid[r][c] = dist

            # explore neighbors
            dfs(r+1, c, dist+1)
            dfs(r-1, c, dist+1)
            dfs(r, c+1, dist+1)
            dfs(r, c-1, dist+1)

        # Start DFS from every gate
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r, c, 0)



        