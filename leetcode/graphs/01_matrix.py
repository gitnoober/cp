
class Solution:
    def updateMatrix(self, mat):
        q = []
        m = len(mat)
        n = len(mat[0])
        dis_arr = [[float('inf') for _ in range(n)] for __ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    continue
                else:
                    dis_arr[i][j] = 0
                    q.append((i,j,0))


        dxdy = [(0,-1),(0,1),(-1,0),(1,0)]
        vis = [[False for _ in range(n)] for __ in  range(m)]

        # for i in q:
        #     print(i, mat[i[0]][i[1]])

        # print()
        # get all the zeroes, and find out the nearest ones


        for i,j,dis in q :
            for dx,dy in dxdy:
                x,y = i+dx, j+dy


                if x < 0 or x >= m or y < 0 or y >= n or vis[x][y] or not mat[x][y]:
                    continue


                vis[x][y] = True
                q.append((x,y,dis+1))
                dis_arr[x][y] = min(dis_arr[x][y] , dis+1)


        return dis_arr


mat = [[0],[1]]
obj = Solution().updateMatrix(mat)
# print(obj)

for i in obj:
    print(i)