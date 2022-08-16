from collections import deque

N = int(input())
for _ in range(N):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # dp = [[-1, -1] for _ in range(2) for __ in range(n)]

    # if a[i] > q:
    #     dp[0][0] = 1
    #     dp[0][1] = q - 1
    # else:
    #     dp[1][0] = 1
    #     dp[1][1] = q
    # res = []

    # def recur(idx, contests_till_now, iq_till_now, path):
    #     if idx == n:
    #         if iq_till_now >= 0:
    #             res.append((contests_till_now, path))
    #         return

    #     # if iq_till_now <= 0:
    #     #     return

    #     recur(
    #         idx + 1,
    #         contests_till_now + 1,
    #         iq_till_now - (a[idx] > iq_till_now),
    #         path + [idx],
    #     )
    #     recur(idx + 1, contests_till_now, iq_till_now, path)

    # # recur(0, 0, q, [])
    # # print(res)
    # q = deque((0,0,q,[]))
    # while q :
    #     idx, contests_till_now, iq_till_now, path = q.popleft()
    cur = 0
    res = [0] * n
    for i in range(n - 1, -1, -1):
        if cur < a[i]:
            if cur < q:
                cur += 1
                res[i] = 1
            else:
                res[i] = 0
        else:
            res[i] = 1
    print("".join(map(str, res)))
