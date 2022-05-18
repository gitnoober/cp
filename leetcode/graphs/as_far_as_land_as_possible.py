
class Solution:
    def maxDistance(self, grid) -> int:
        # start from the land and see how deep you can get
        vis = set()
        dxdy = [(0,-1),(0,1),(-1,0),(1,0)]
        n = len(grid)

        # def dfs(x,y):
        #     vis.add((x,y))
        #     for dx,dy in dxdy:
        #         i,j=x+dx,y+dy
        #         if i < 0 or i >= n or j < 0 or j >=n or (i,j) in vis:
        #             continue
        #         dfs(i,j)
        q = []
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i,j,0))

        ans = -1
        level = 0

        for i,j,dis in q :
            for dx,dy in dxdy:
                x,y = i+dx, j+dy
                if x < 0 or x >= n or y < 0 or y >= n or grid[x][y]:
                    continue
                grid[x][y]=1
                q.append((x,y,dis+1))
                ans = max(ans, dis+1)

        return ans


grid = [[1,0,1],[0,0,0],[1,0,1]]
obj = Solution().maxDistance(grid)
print(obj)