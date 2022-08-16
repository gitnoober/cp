def getSum(BITree: list, index: int) -> int:
    summ = 0  # Initialize result
    index = index + 1
    while index > 0:
        summ += BITree[index]
        index -= index & (-index)
    return summ


def updateBit(BITTree: list, n: int, index: int, val: int) -> None:
    index = index + 1
    while index <= n:
        BITTree[index] += val
        index += index & (-index)


def summation(x: int, BITTree1: list, BITTree2: list) -> int:
    return (getSum(BITTree1, x) * x) - getSum(BITTree2, x)


def updateRange(
    BITTree1: list, BITTree2: list, n: int, val: int, l: int, r: int
) -> None:
    updateBit(BITTree1, n, l, val)
    updateBit(BITTree1, n, r + 1, -val)
    updateBit(BITTree2, n, l, val * (l - 1))
    updateBit(BITTree2, n, r + 1, -val * r)


def rangeSum(l: int, r: int, BITTree1: list, BITTree2: list) -> int:
    return summation(r, BITTree1, BITTree2) - summation(l - 1, BITTree1, BITTree2)


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        BITTree1 = [0] * (n + 1)
        BITTree2 = [0] * (n + 1)
        ans, mx = [], n - 1
        for __ in range(n):
            l, r = map(lambda x: int(x) - 1, input().split())

            if l <= __ <= r:
                if __ > 0 and __ - 1 >= l:
                    updateRange(BITTree1, BITTree2, n, 1, l, __ - 1)
                if __ + 1 <= r and __ + 1 < n:
                    updateRange(BITTree1, BITTree2, n, 1, __ + 1, r)

            else:
                updateRange(BITTree1, BITTree2, n, 1, l, r)

        for i in range(n):
            if i == 0:
                s = rangeSum(0, 0, BITTree1, BITTree2)
            else:
                x = rangeSum(0, i, BITTree1, BITTree2)
                y = rangeSum(0, i - 1, BITTree1, BITTree2)
                s = x - y

            # if i == n - 1:
            #     print(s, x, y)

            if s >= mx:
                ans.append(i + 1)
        # print(ans)

        print(len(ans))
        print(*ans, sep="\n")
