def rot_90(l):
    return [list(reversed(x)) for x in zip(*l)]


from copy import deepcopy

N = int(input())

for _ in range(N):
    n = int(input())
    a = [[int(j) for j in input()] for __ in range(n)]
    ARR = deepcopy(a)
    # print(a)
    arr = []
    A = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append((i + 1, j + 1, a[i][j]))
        A.append(x)

    arr.append(A[::])
    for r in range(3):
        arr.append(rot_90(arr[-1]))

    a = []
    cnt = 0
    for j in range(n):
        for k in range(n):
            x = []
            y = []
            for i in arr:
                # x.append(i[j][k])
                xx = i[j][k][0]
                yy = i[j][k][1]
                y.append(i[j][k])
                x.append(ARR[xx - 1][yy - 1])

            if len(set(x)) == 1:
                continue
            ones = x.count(1)
            zeroes = 4 - ones
            op = 0
            if 4 - ones <= 4 - zeroes:
                op = 1

            for xx, yy, vv in y:
                ARR[xx - 1][yy - 1] = 1

            # print(x)
            cnt += min(4 - ones, 4 - zeroes)

    print(cnt)

    # for i in range(n):
    #     for j in range(n):
    #         x = []
    #         for f in range(4):
    #             x.append(arr[f][i][j])
    #         if len(set(x)) == 1:
    #             continue
    #         ones = x.count(1)
    #         cnt += min(4 - ones, 4 - (4 - ones))
    #         print(x, min(4 - ones, 4 - (4 - ones)))
    # print(cnt)
