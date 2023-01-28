class Solution:
    def snakesAndLadders(self, board) -> int:
        rc_map = {}
        n = len(board)
        r, c = n - 1, 0
        ev = 0
        prev = 1
        for i in range(n, n * n + 1, n):
            if ev % 2 == 0:
                for j in range(prev, i + 1):
                    rc_map[j] = [r, c]
                    c += 1
                c -= 1
            else:
                for j in range(prev, i + 1):
                    rc_map[j] = [r, c]
                    c -= 1
                c += 1
            prev = i + 1
            ev += 1
            r -= 1
        stack = [(1, 0)]  # start sqaure
        dist = [-1 for _ in range(n * n + 1)]
        dist[1] = 0
        for curr, dis in stack:
            for nxt in range(curr + 1, min(curr + 6, n * n) + 1):
                r, c = rc_map[nxt]
                dest = board[r][c] if board[r][c] != -1 else nxt

                if dist[dest] == -1:
                    dist[dest] = dist[curr] + 1
                    stack.append((dest, dist[dest]))

        return dist[n * n]


board = [[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]
board = [[-1, 4, -1], [6, 2, 6], [-1, 3, -1]]
board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]


obj = Solution().snakesAndLadders(board)
print(obj, "obj")
"""
16 15 14 13
9 10 11 12
8 7 6 5
1 2 3 4
"""
#    1      1      1      2
# 1 -- > 7 --> 10 --> 13 --> 16
