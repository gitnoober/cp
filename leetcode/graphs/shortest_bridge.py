class Solution:
    def shortestBridge(self, grid) -> int:
        n, dxdy, vis, q = len(grid), [(0, -1), (0, 1), (-1, 0), (1, 0)], set(), []
        dist_arr = [[float("inf") for _ in range(n)] for __ in range(n)]
        ans = float("inf")

        def dfs(i, j):
            vis.add((i, j))
            grid[i][j] = -1

            for x, y in dxdy:
                xx, yy = x + i, y + j
                if (
                    xx < 0
                    or yy < 0
                    or xx >= n
                    or yy >= n
                    or (xx, yy) in vis
                    or not grid[xx][yy]
                ):
                    continue

                dfs(xx, yy)

        def mark():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        dfs(i, j)
                        return

        mark()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == -1:
                    q.append((i, j, 0))

        for i, j, dis in q:
            for dx, dy in dxdy:
                x, y = i + dx, j + dy
                if x >= 0 and x < n and y >= 0 and y < n and (x, y) not in vis:
                    if grid[x][y] == -1:
                        continue

                    dist_arr[x][y] = min(dis + 1, dist_arr[x][y])
                    q.append((x, y, dist_arr[x][y]))
                    vis.add((x, y))
                    if grid[x][y] == 1:
                        ans = min(ans, dist_arr[x][y] - 1)

        return ans


# connect two islands by converting 0's to 1's


grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
obj = Solution().shortestBridge(grid)
print(obj)
