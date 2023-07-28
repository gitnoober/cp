class Solution:
    def latestDayToCross(self, n: int, m: int, cells: List[List[int]]) -> int:
        dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def check(till):
            A = [[0] * m for __ in range(n)]
            for i in range(till):
                r, c = cells[i]
                A[r - 1][c - 1] = 1

            q = []
            for i in range(m):
                if not A[0][i]:
                    q.append((0, i))
                    A[0][i] = 1

            for i, j in q:
                if i == n - 1:
                    return True

                for dx, dy in dxdy:
                    X, Y = i + dx, j + dy
                    if X > -1 and X < n and Y > -1 and Y < m and not A[X][Y]:
                        q.append((X, Y))
                        A[X][Y] = 1
            return False

        l, h = 1, len(cells)
        ans = 0
        print(check(2))
        print(check(3))
        while l <= h:
            m = (l + h) // 2
            if check(m):
                print("true", m)
                ans = m
                l = m + 1
            else:
                h = m - 1
        return ans
