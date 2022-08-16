N = int(input())
for _ in range(N):
    n = int(input())
    nums = list(map(int, input().split()))
    res = []
    for __ in range(n):
        num, moves = input().split()
        num = nums[__]
        up, down = 0, 0
        for j in moves:
            if j == "U":
                up += 1
            else:
                down += 1
        up %= 10
        down %= 10
        while down > 0:
            num += 1
            num %= 10
            down -= 1

        while up > 0:
            up -= 1
            num -= 1
            if num == -1:
                num = 9
        res.append(num)
    print(*res)
