from collections import deque
import sys

init_calorie = int(input())
jump_calorie = int(input())
coins_calorie = int(input())
m, n = map(int, input().split())  # row , col
arr = deque()
for i in range(m):
    arr.appendleft(list(input()))

i, ans = 0, 0
while i < n:
    if init_calorie == 0:
        i -= 1
        break

    idx1, idx2, cnt, obstacle = 0, 0, 0, False
    zero = False
    for j in range(m):
        if arr[j][i] == "C":
            cnt += 1
            idx1 = j
        elif arr[j][i] == "H":
            if not zero:
                idx2 = j
                obstacle = True
        else:
            if obstacle:
                zero = True

    if not obstacle:
        # no H, so you skip this or take all coins
        # print(cnt, coins_calorie, idx1, jump_calorie)
        if (
            cnt > 0
            and cnt * coins_calorie >= idx1 * jump_calorie
            and init_calorie >= idx1 * jump_calorie
        ):
            init_calorie -= idx1 * jump_calorie
            init_calorie += coins_calorie * cnt
        else:
            init_calorie -= 1
    else:
        jumps = idx2 + 1
        # print(jumps, obstacle, i + 1)
        init_calorie -= jumps * jump_calorie
        if init_calorie < 0:
            i -= 1
            break
        init_calorie += coins_calorie * cnt
        if jumps == 0 and init_calorie == 0:
            i -= 1
            break
    # print(init_calorie, i + 1, obstacle)
    i += 1

# print("sx", i, n)
if i == n:
    sys.stdout.write(str(init_calorie))
else:
    sys.stdout.write(str(i))


"""5
1
2
5 10
0000000000
0CCC00000H
0CCC0H0000
00000H0H0H
00000H0H0H

"""


"""
    obstacle = False
    idx = None
    for j in range(m):
        if arr[j][i] == "H":
            obstacle = True
            idx = j

    if not obstacle:
        idx = None
        cnt = 0
        for j in range(m):
            if arr[j][i] == "C":
                idx = j
                cnt += 1
        if idx == None:
            if init_calorie == 0:
                i -= 1
                break
            init_calorie -= 1
        else:
            init_calorie -= idx * jump_calorie
            if init_calorie < 0:
                i -= 1
                break
            init_calorie += coins_calorie * cnt
    else:
"""
