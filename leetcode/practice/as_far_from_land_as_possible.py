class Solution:
    def maxDistance(self, grid) -> int:
        ans = -1
        vis = set()
        adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        n = len(grid)
        dist = [[float("inf") for _ in range(n)] for __ in range(n)]
        st = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    st.append((i, j, 0))
                    vis.add((i, j))

        for x, y, dis in st:
            for dx, dy in adj:
                X, Y = x + dx, y + dy
                if X >= 0 and X < n and Y >= 0 and Y < n and (X, Y) not in vis:
                    dist[X][Y] = min(dist[X][Y], dis + 1)
                    vis.add((X, Y))
                    if grid[X][Y] == 0:
                        st.append((X, Y, dist[X][Y]))
                        ans = max(ans, dist[X][Y])

        return ans


# grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
obj = Solution().maxDistance(grid)
print(obj)


def disable_comment_of_user(uid=None, entity_id=None, entity_type=None):
    mongo_con = mongo_connection()
    db = mongo_con.social
    comment_collection = db.comments
    query = {
        "comment_creator_uid": uid,
        "story_id": entity_id,
        "entity_type": entity_type,
    }
    comment_collection.update(query, {"$set": {"is_enable": False}})
    return True


query = {"comment_creator_uid": uid, "story_id": entity_id, "entity_type": entity_type}
