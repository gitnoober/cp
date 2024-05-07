# from collections import defaultdict
# def min_time (N, cards, queries):

#     def subsets(nums):
#         nums.sort()
#         result = [[]]
#         for num in nums:
#             result += [i + [num] for i in result]

#         return [sum(i) for i in result]

#     # x = subsets(cards)
#     # print(x)
#     res = []

#     for l,r,q in queries:
#         arr = cards[l-1:r]
#         all_sum = subsets(arr)
#         freqs = defaultdict(int)
#         for i in all_sum:
#             freqs[i]+=1
#         num = q
#         for k in range(64,-1,-1):
#             if (1<<k)&q and freqs[(1<<k)]:
#                 freqs[(1<<k)]-=1
#                 num-=(1<<k)

#         if num == 0:
#             res.append(0)
#         elif max(all_sum) < q :


# N = int(input())
# cards = list(map(int, input().split()))
# Q = int(input())
# queries = [list(map(int, input().split())) for i in range(Q)]

# out_ = min_time(N, cards, queries)
# print (' '.join(map(str, out_)))


from itertools import combinations

a = list(range(1, 10)) + list(range(1, 10)) + list(range(1, 10))
se = set()
for i in combinations(a, 4):
    if sum(i) == 7:
        ok = True
        for j in i:
            if j > 3:
                ok = False
        if ok:
            # print(i)
            se.add(i)

# print(len(se))
for i in se:
    print(i)
