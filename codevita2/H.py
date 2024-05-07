import sys

n = int(input())
gr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    gr[u].append(v)

# vis = [0]*(n+1)
# start = [None]*(n+1)
# end = [None]*(n+1)
# order = [None]

# def dfs(a,b):
# 	vis[a] = 1
# 	b +=1
# 	start[a] = b
# 	order.append(a)

# 	for u in gr[a]:
# 		if not vis[u]:
# 			b = dfs(u,b)
# 	end[a] = b
# 	return b

# dfs(1,1)
# sub_tree = defaultdict(list)
# def Print(n):
#     for i in range(0, n):
#         if start[i] != end[i]:
#             for j in range(start[i]+1, end[i]+1):
#                 sub_tree[i].append(order[j-1])
# Print(n)
# print(sub_tree)
checked = [1] * (n + 1)
visi = [0] * (n + 1)


def recur(node, gcd_goal):
    visi[node] = 1
    p = gcd_goal
    for child in gr[node]:
        if not visi[child]:
            # print(child,p)
            checked[child] = p
            recur(child, p)
            p += gcd_goal


recur(1, 1)
# print(checked)
mul = 1
mod = int(1e9) + 7
for i in checked:
    mul *= i
sys.stdout.write(str(mul % mod))
