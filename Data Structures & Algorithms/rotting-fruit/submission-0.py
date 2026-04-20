from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0
        q = deque()
        time = 0

        def bfs(row, col):
            nonlocal freshCount
            if min(row, col) < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            
            if grid[row][col] == 1:
                freshCount -= 1
                grid[row][col] = 2
                q.append((row, col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    freshCount += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        while q and freshCount:
            for _ in range(len(q)):
                row, col = q.popleft()
                bfs(row + 1, col)
                bfs(row - 1, col)
                bfs(row, col + 1)
                bfs(row, col - 1)
            time += 1
        
        if freshCount:
            return -1
        else:
            return time
        



