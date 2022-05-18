
class Solution:
    def pacificAtlantic(self, heights):
        
        self.r,self.c = len(heights), len(heights[0])
        self.dxdy = [(0,-1), (0,1) , (1,0),(-1,0)]
        self.a = [[False for _ in range(self.c)] for __ in range(self.r)]
        self.b = [[False for _ in range(self.c)] for __ in range(self.r)]

        def dfs(x,y,vis):
            vis[x][y] = True

            for dx , dy in self.dxdy:
                i,j = x + dx, y + dy

                if i < 0 or j < 0 or i >= self.r or j >= self.c or vis[i][j] or heights[x][y] > heights[i][j]:
                    continue
                dfs(i,j,vis)


        for i in range(self.r):
            dfs(i,0,self.a)
            dfs(i,self.c-1, self.b)

        for j in range(self.c):
            dfs(0,j,self.a)
            dfs(self.r-1,j,self.b)
        ans = []

        for i in range(self.r):
            for j in range(self.c):
                if self.a[i][j] and self.b[i][j]:
                    ans.append([i,j])
        return ans

heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
obj = Solution().pacificAtlantic(heights)
print(obj)
