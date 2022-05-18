

class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        vis = [False]*n
        q = [0]
        vis[0]=True
        for i in q:
            for u in rooms[i]:
                if vis[u]:
                    continue
                vis[u] = True
                q.append(u)

        ok = True
        # print(vis)
        for i in range(n):
            if not vis[i]:
                ok = False

        return ok

rooms = [[1,3],[3,0,1],[2],[0]]
obj = Solution().canVisitAllRooms(rooms)
print(obj)