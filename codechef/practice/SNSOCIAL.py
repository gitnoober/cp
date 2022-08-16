for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    q, mx, vis, dxdy, ans = (
        [],
        0,
        set(),
        [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)],
        0,
    )
    for i in range(n):
        for j in range(m):
            if arr[i][j] > mx:
                mx = arr[i][j]
                q.clear()
                vis.clear()

            if arr[i][j] == mx:
                q.append((i, j, 0))
                vis.add((i, j))

    for x, y, d in q:
        for dx, dy in dxdy:
            X, Y = x + dx, y + dy
            if (
                X > -1
                and X < n
                and Y > -1
                and Y < m
                and (X, Y) not in vis
                and arr[X][Y] < arr[x][y]
            ):
                vis.add((X, Y))
                q.append((X, Y, d + 1))
                ans = max(ans, d + 1)
                arr[X][Y] = arr[x][y]
    print(ans)
