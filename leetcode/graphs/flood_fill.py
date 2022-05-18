class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        q = [(sr,sc)]
        dxdy = [(0,-1), (0,1), (-1,0), (1,0)]
        color = image[sr][sc]
        vis = set()
        n,m = len(image), len(image[0])
        for i,j in q :
            for dx,dy in dxdy:
                x,y = i+dx, j + dy
                if x > -1 and x < n and y > -1 and y < m and (x,y) not in vis:
                    image[x][y] = newColor
                    q.append((x,y))
            vis.add((i,j))
            
        image[sr][sc] = newColor
        return image


