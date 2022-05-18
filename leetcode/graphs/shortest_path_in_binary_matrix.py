
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        
        q = [(0,0,1)]
        dxdy = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1)]
        n = len(grid)
        vis = [[False for _ in range(n)] for __ in range(n)]
        ans = float('inf')

        if n == 1 and not grid[0][0]:
            ans = 1

        for i,j,dis in q:
            if grid[i][j]:
                continue
            for dx,dy in dxdy:
                x,y=i+dx,j+dy
                if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] or vis[x][y]:
                    continue

                vis[x][y] = True
                q.append((x,y,dis+1))

                if x == n -1 and y == n - 1:
                    ans = min(ans, dis+1)

        return -1 if ans == float('inf') else ans





grid = [[0]]
obj = Solution().shortestPathBinaryMatrix(grid)
print(obj)