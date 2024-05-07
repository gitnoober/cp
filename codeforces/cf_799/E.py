import sys


def lenOfLongSubarr(A, N, K):

    i, j, sum = 0, 0, 0
    maxLen = -sys.maxsize - 1

    while j < N:
        sum += A[j]
        if sum < K:
            j += 1
        elif sum == K:
            maxLen = max(maxLen, j - i + 1)
            j += 1
        elif sum > K:
            while sum > K:
                sum -= A[i]
                i += 1
            if sum == K:
                maxLen = max(maxLen, j - i + 1)
            j += 1
    return maxLen


for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    x = lenOfLongSubarr(a, n, s)
    if x == -sys.maxsize - 1:
        print(-1)
    else:
        print(n - x)
