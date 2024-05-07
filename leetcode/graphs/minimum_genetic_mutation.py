class Solution:
    def minMutation(self, start: str, end: str, bank):

        vis = set()
        q = [(start, 0)]
        dic = {j: 1 for j in bank}
        dist = {start: 0}

        ok = False
        for gene, dis in q:
            l = len(gene)
            for j in range(l):
                for k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    st = gene[:j] + k + gene[j + 1 :]
                    if st in vis or st not in dic:
                        continue

                    q.append((st, dis + 1))
                    vis.add(st)
                    dist[st] = dis + 1
                    if st == end:
                        ok = True
                        break
            if ok:
                break

        return dist[end] if end in dist else -1


start = "AACCTTGG"
end = "AATTCCGG"
bank = ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]
obj = Solution().minMutation(start, end, bank)
print(obj)
# "AACCTTGG"
# "AATTCCGG"
# ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
