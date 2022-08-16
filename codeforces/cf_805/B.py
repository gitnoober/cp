N = int(input())
for _ in range(N):
    s = input()
    vis = set()
    cnt = 0
    res = 0
    for i in s:
        if i in vis:
            continue
        if cnt == 3:
            cnt = 0
            res += 1
            vis.clear()
        vis.add(i)
        cnt += 1

    if cnt:
        res += 1
    print(res)
