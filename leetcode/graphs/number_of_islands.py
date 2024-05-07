class Solution:
    def numIslands(self, grid) -> int:
        cnt = 1
        n, m = len(grid), len(grid[0])
        vis = set()
        dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(i, j):
            nonlocal vis
            vis.add((i, j))
            for dx, dy in dxdy:
                x, y = i + dx, j + dy
                if (
                    x > -1
                    and x < n
                    and y > -1
                    and y < m
                    and (x, y) not in vis
                    and grid[x][y] == "1"
                ):
                    dfs(x, y)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in vis and grid[i][j] == "1":
                    dfs(i, j)
                    vis.add((i, j))
                    cnt += 1
        return cnt


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
obj = Solution().numIslands(grid)
