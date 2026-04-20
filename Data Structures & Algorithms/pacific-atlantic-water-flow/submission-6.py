class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacificBorder = []
        atlanticBorder = []
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacificBorder.append((i, j))
                if i == m - 1 or j == n - 1:
                    atlanticBorder.append((i, j))
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def dfs(i, j):
            if (i, j) in res:
                return
            res.add((i, j))
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                
                if (nr, nc) in res:
                    continue

                if heights[i][j] <= heights[nr][nc]:
                    dfs(nr, nc)
            return
        res = set()
        for i, j in pacificBorder:
            dfs(i, j)
        pacificFlow = res
        res = set()
        for i, j in atlanticBorder:
            dfs(i, j)
        atlanticFlow = res
        print(pacificFlow)
        print(atlanticFlow)
        return list(atlanticFlow & pacificFlow)
