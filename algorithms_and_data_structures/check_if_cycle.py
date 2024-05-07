def find_cycle(graph):
    n = len(graph)
    [False] * n
    color = [0] * n

    def dfs(u, p):
        color[u] = 1
        # cnt[0]+=1
        # print(u, "vertices")
        for w in graph[u]:
            if color[w] == 1 and w != p:
                return False
            if color[w] == 0 and not dfs(w, u):
                return False

        color[u] = 2
        return True

    for i in range(n):
        if color[i] == 0 and not dfs(i, -1):
            return False
    return True


"""
Find the largest cycle
"""


def find_largest_cycle(graph):
    n = len(graph)
    [False] * n
    color = [0] * n
    cnt = [0]

    def dfs(u, p):
        color[u] = 1
        cnt[0] += 1
        for w in graph[u]:
            if color[w] == 1 and w != p:
                return False
            if color[w] == 0 and not dfs(w, u):
                return False

        color[u] = 2
        return True

    ans = 1
    for i in range(n):
        color = [0] * n
        dfs(i, -1)
        ans = max(ans, cnt[0])
        cnt[0] = 0
    return ans


# n = 5
# graph = [[] for _ in range(n)]
# graph[0].append(1)
# graph[1].append(2)
# graph[1].append(3)
# graph[2].append(4)
# graph[4].append(0)
# graph[3].append(2)
# x = find_largest_cycle(graph)
# print(x)
# tc = int(input())
# n = int(input())
# a = list(map(int, input().split()))
# graph = [[] for _ in range(n)]
# for i in range(n):
#     if a[i] == - 1:
#         continue
#     graph[i].append(a[i])
# x = find_largest_cycle(graph)
# print(x)
