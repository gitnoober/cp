class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        n, m, res, dxdy = len(grid), len(grid[0]), 0, [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(i, j):
            res = 0
            if i >= 0 and i < n and j >= 0 and j < m and grid[i][j]:
                grid[i][j] = 0
                res += 1
                for x, y in dxdy:
                    res += dfs(x + i, y + j)
            return res

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
obj = Solution().maxAreaOfIsland(grid)
print(obj)
