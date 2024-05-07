class Solution:
    def nearestExit(self, maze, entrance) -> int:
        dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        q = [[entrance[0], entrance[1], 0]]
        m, n = len(maze), len(maze[0])
        dist_arr = [[float("inf") for _ in range(n)] for __ in range(m)]
        ans = float("inf")
        dist_arr[entrance[0]][entrance[1]] = 0

        for i, j, dis in q:
            for dx, dy in dxdy:
                x, y = i + dx, j + dy
                if (
                    x >= 0
                    and x < m
                    and y >= 0
                    and y < n
                    and dist_arr[x][y] == float("inf")
                    and maze[x][y] == "."
                ):
                    dist_arr[x][y] = min(dis + 1, dist_arr[x][y])
                    q.append((x, y, dist_arr[x][y]))

                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        ans = min(ans, dist_arr[x][y])

        return ans if ans != float("inf") else -1


maze = [
    ["+", ".", "+", "+", "+", "+", "+"],
    ["+", ".", "+", ".", ".", ".", "+"],
    ["+", ".", "+", ".", "+", ".", "+"],
    ["+", ".", ".", ".", "+", ".", "+"],
    ["+", "+", "+", "+", "+", ".", "+"],
]
entrance = [0, 1]
obj = Solution().nearestExit(maze, entrance)
print(obj)
