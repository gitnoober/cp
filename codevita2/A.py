import sys

s = input()
N = (10**5) + 5
# N = 5
clean = [[] for _ in range(N)]
l = len(s)
n = 1
for i in range(l):
    if s[i] == " ":
        continue
    # print(s[i])
    if s[i] == "{":
        x = int(s[i - 2])
        j = i + 1
        n = max(n, x)
        while j < l and s[j] != "}":
            if s[j] != ",":
                clean[int(s[j])].append(x)
                n = max(n, int(s[j]))
            j += 1


# print(s)
# print(n)
# print(clean)
qq = []


def check_cycle(n):
    # print(clean)
    in_degree = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in clean[i]:
            in_degree[j] += 1
            # print(j,clean[i])

    q = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
            qq.append((i, 1))

    cnt = 0
    for node in q:

        for child in clean[node]:
            in_degree[child] -= 1

            if in_degree[child] == 0:
                q.append(child)
        cnt += 1

    # print(cnt,n)
    if cnt != n:
        return True
    return False


if check_cycle(n):
    sys.stdout.write("error")
else:
    ans = 1
    # print(qq)
    vis = set()
    for node, dis in qq:
        for child in clean[node]:
            if child in vis:
                continue

            vis.add(child)
            qq.append((node, dis + 1))
            ans = max(ans, dis + 1)
    # print(ans)
    sys.stdout.write(str(ans))


# for node in range(n+1):
# 	if not vis[node]:


"""
1.{}, 2.{}, 3.{1,2}

1.{}, 2.{1,4}, 3.{2}, 4.{3}
"""
