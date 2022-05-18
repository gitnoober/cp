class Solution:
    def numEnclaves(self, grid) -> int:
        vis, dxdy = set() , [(0,-1), (0,1), (1,0), (-1,0)]
        m,n = len(grid), len(grid[0])

        def dfs(i,j):
            vis.add((i,j))
            grid[i][j] = 0
            for x,y in dxdy:
                X,Y = x+i, y+j
                if X > -1 and X < m and Y > -1 and Y < n and (X,Y) not in vis and grid[X][Y]:
                    dfs(X,Y)


        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    dfs(i,j)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cnt+=1
        return cnt


grid = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
obj = Solution().numEnclaves(grid)
print(obj)