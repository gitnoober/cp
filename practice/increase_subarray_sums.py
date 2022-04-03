import sys


def input():
    return sys.stdin.readline().rstrip("\r\n")


def maps():
    return [int(i) for i in input().split()]


# lOOKOUT FOR THE EDGE CASES
for _ in range(int(input())):
    n, x = maps()
    a = maps()
    ok, cur_sum, max_sum = True, 0, 0
    end_idx = n - 1

    for i in range(n):
        if a[i] < 0:
            ok = False
        cur_sum += a[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            end_idx = i
        elif cur_sum < 0:
            cur_sum = 0
    if ok:
        print(*[max_sum + i * x for i in range(n + 1)])
    else:
        lzy = [-float("inf")] * (n + 1)
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += a[j]
                lzy[j - i + 1] = max(lzy[j - i + 1], cur_sum)
        res = []
        # iterate over every length and find out the maximum value
        for k in range(n + 1):
            bst = 0
            for i in range(n + 1):
                bst = max(
                    bst, lzy[i] + min(i, k) * x
                )  # length 0 , 1 , 2 , 3 , 4 .... with max k *x
            res.append(bst)
        print(" ".join(map(str, res)))
