def calculate_median(n):
    N = len(n)
    n.sort()
    if N % 2 == 0:
        return n[N // 2 - 1]
    else:
        return n[N // 2]


# arr = [3, 1, 2]
# print(calculate_median(arr))


def brute(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != calculate_median(arr[: i + 1]):
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    # a = list(range(1, n + 1))
    # for i in permutations(a):
    #     if brute(list(i)):
    #         print(i)
    ans = []
    i, j = n, 1
    while len(ans) < n:
        ans.append(i)
        ans.append(j)
        i -= 1
        j += 1
    print(*ans[:n])
