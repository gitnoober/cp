def findClosest(a, target):
    n = len(a)
    if target >= a[n - 1]:
        return (a[n - 1], n - 1)
    if target <= a[0]:
        return (a[0], 0)

    i, j = 0, n
    while i < j:
        m = (i + j) >> 1
        if a[m] == target:
            return a[m]

        elif target < a[m]:
            j = m
            if m > 0 and target > a[m - 1]:
                return getClosest(a[m - 1], a[m], target)

        else:
            if m < n - 1 and target < a[m + 1]:
                return getClosest(a[m], a[m + 1], target)
            i = m + 1

    return (a[m], m)


def getClosest(a, b, target):
    if target - a >= target - b:
        return b
    return a


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = abs(a[0] - b[0]) + abs(a[-1] - b[-1])
    vis, s = set(), 0
    a.sort()
    b.sort()
    for i in range(n):
        x = findClosest(b, a[i])
        y = findClosest(a,b[i])
        if x[]
    ans = min(ans, s)
    print(ans)

    """
    Either the first option or find the closest element 
    """
