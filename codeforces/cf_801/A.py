def check(h, w, arr, n, m):
    se = set()
    for i in range(n - h + 1):
        for j in range(m - w + 1):
            mx = -float("inf")
            for ii in range(i, i + h):
                for jj in range(j, j + w):
                    mx = max(arr[ii][jj], mx)
            se.add(mx)
            if len(se) > 1:
                break
        if len(se) > 1:
            break

    return len(se) == 1


for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = float("inf")

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if check(r, c, arr, n, m):
                res = min(res, r * c)
    print(res)
