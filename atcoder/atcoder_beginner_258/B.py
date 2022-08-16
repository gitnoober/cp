dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
n = int(input())
arr = [list(input()) for _ in range(n)]


def func(x, y, dir):
    c = n - 1
    st = arr[x][y]
    while c:
        x, y = (x + dir[0]) % n, (y + dir[1]) % n
        st += arr[x][y]
        c -= 1
    return int(st)


ans = 0
for i in range(n):
    for j in range(n):
        for dir in dxdy:
            ans = max(ans, func(i, j, dir))

print(ans)
