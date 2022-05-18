

class Solution:
    def countSubIslands(self, grid1, grid2):

        dxdy = [(0,-1),(0,1),(-1,0),(1,0)]
        vis = set()
        global_vis = set()
        m,n = len(grid1), len(grid1[0])

        def dfs(i,j):
            vis.add((i,j))
            global_vis.add((i,j))

            for x,y in dxdy:
                X,Y = x + i, j + y
                if X > -1 and X < m and Y > -1 and Y < m and (X,Y) not in vis and grid2[X][Y]:
                    dfs(X,Y)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] and (i,j) not in global_vis:
                    dfs(i,j)
                    ok = True
                    for x,y in vis:
                        if not grid1[x][y]:
                            ok = False
                            break
                    if ok :
                        ans+=1
                    vis.clear()
        return ans



"""
brute force 
have all the islands in grid1


"""

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]

obj = Solution().countSubIslands(grid1, grid2)
print(obj)