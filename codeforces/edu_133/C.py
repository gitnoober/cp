# lOOKOUT FOR THE EDGE CASES
from collections import deque


def sol():
    m = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    pr1, pr2 = [0], [0]

    def brute():
        q = deque()
        q.append((0, 0, {(0, 0)}, 0))
        dxdy = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        ans = float("inf")

        while q:
            i, j, vis, time = q.popleft()
            for dx, dy in dxdy:
                x, y = i + dx, j + dy
                if x >= 0 and x < 2 and y >= 0 and y < m and (x, y) not in vis:
                    if time >= arr[x][y]:
                        t = time + 1
                    else:
                        t = arr[x][y] + 1
                    if t >= ans:
                        continue

                    vis_s = vis.copy()
                    vis_s.add((x, y))
                    q.append((x, y, vis_s, t))
                    if len(vis_s) == 2 * m:
                        ans = min(ans, t)
                        # print(sorted(vis_s), t)
        # print(ans)
        return ans

    def func1():
        ans = 0
        # ans = arr[0][0] + 1 if arr[0][0] != 0 else 0

        for i in range(1, m):
            if ans >= arr[0][i]:
                ans = ans + 1
            else:
                ans = arr[0][i] + 1
            pr1.append(ans)
        # print(ans, "ans")

        if ans >= arr[1][-1]:
            ans += 1
        else:
            ans = arr[1][-1] + 1
        pr1.append(ans)
        # print(ans)

        for i in range(m - 2, -1, -1):
            if ans >= arr[1][i]:
                ans += 1
            else:
                ans = arr[1][i] + 1
        pr1.append(ans)
        # print(ans)
        return ans

    def func2():
        ans = 0
        # ans = arr[0][0] + 1 if arr[0][0] != 0 else 0
        if ans >= arr[1][0]:
            ans += 1
        else:
            ans = arr[1][0] + 1
        pr2.append(ans)

        for i in range(1, m):
            if ans >= arr[1][i]:
                ans += 1
            else:
                ans = arr[1][i] + 1
            pr2.append(ans)

        if ans >= arr[0][-1]:
            ans += 1
        else:
            ans = arr[0][-1] + 1
        pr2.append(ans)

        for i in range(m - 2, 0, -1):
            if ans >= arr[0][i]:
                ans += 1
            else:
                ans = arr[0][i] + 1
            pr2.append(ans)
        return ans

    def func3():
        # ans = arr[0][0]
        # ans = arr[0][0] + 1 if arr[0][0] != 0 else 0
        ans = 0
        x = 1
        for i in range(m - 1):
            if i == 0:
                # down
                if ans >= arr[x][i]:
                    ans += 1
                else:
                    ans = arr[x][i] + 1

                # right
                if ans >= arr[x][i + 1]:
                    ans += 1
                else:
                    ans = arr[x][i + 1] + 1

                # up
                x ^= 1
                if ans >= arr[x][i + 1]:
                    ans += 1
                else:
                    ans = arr[x][i + 1] + 1
            else:
                # right
                if ans >= arr[x][i + 1]:
                    ans += 1
                else:
                    ans = arr[x][i + 1] + 1

                # down
                x ^= 1
                if ans >= arr[x][i + 1]:
                    ans += 1
                else:
                    ans = arr[x][i + 1] + 1
        return ans

    def func4():
        ans = 0
        # ans = arr[0][0] + 1 if arr[0][0] != 0 else 0
        x = 1
        all_ans = float("inf")
        for i in range(m - 1):
            if i == 0:
                # down
                if ans >= arr[x][i]:
                    ans += 1
                else:
                    ans = arr[x][i] + 1

                # right
                if ans >= arr[x][i + 1]:
                    ans += 1
                else:
                    ans = arr[x][i + 1] + 1

                # up
                x ^= 1
                if ans >= arr[x][i + 1]:
                    ans += 1
                else:
                    ans = arr[x][i + 1] + 1
            else:
                # if i == m - 3:
                # print(ans, i, pr1)
                # if ans >= arr[x][i + 1]:
                #     ans += 1
                # else:
                #     ans = arr[x][i + 1] + 1

                # if ans >= arr[x][i + 2]:
                #     ans += 1
                # else:
                #     ans = arr[x][i + 2] + 1

                # x ^= 1
                # if ans >= arr[x][i + 2]:
                #     ans += 1
                # else:
                #     ans = arr[x][i + 2] + 1

                # if ans >= arr[x][i + 1]:
                #     ans += 1
                # else:
                #     ans = arr[x][i + 1] + 1

                # break
                if i % 2 == 0:
                    all_ans = min(ans + pr1[i], all_ans)
                else:
                    # print(ans, i, pr2[-i])
                    all_ans = min(max(ans, pr2[-i]), all_ans)
                #     all_ans = min(ans + pr2[i], all_ans)

                # right
                if ans >= arr[x][i + 1]:
                    ans += 1
                else:
                    ans = arr[x][i + 1] + 1

                # down
                x ^= 1
                if ans >= arr[x][i + 1]:
                    ans += 1
                else:
                    ans = arr[x][i + 1] + 1
        # return ans
        return min(all_ans, ans)

    # x = func3(arr)
    # print(x, arr[::-1])
    # print(x)
    ans1 = brute()
    ans2 = min(func1(), func2(), func3(), func4())
    # print(ans2)
    if ans1 != ans2:
        print(arr[0], "\n", arr[1], ans1, ans2)
        print(func1(), "---- func1")
        print(func2(), "----func2")
        print(func3(), "----func3")
        print(func4(), "----func4")

    # else:
    # q.append


tc = int(input())
while tc:
    sol()
    tc -= 1
