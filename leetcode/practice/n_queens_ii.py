

class Solution:
    def totalNQueens(self, n: int) -> int:


        diag1, diag2, vis = set(), set(), set()
        self.ans = 0

        def recur(diag1, diag2, vis, row):
            
            if row == n :
                self.ans += 1

            for j in range(n):
                if row+j in diag1 or row-j in diag2 or j in vis:
                    continue

                diag1.add(row+j)
                diag2.add(row-j)
                vis.add(j)

                recur(diag1, diag2, vis, row+1)

                diag1.remove(row+j)
                diag2.remove(row-j)
                vis.remove(j)

        recur(diag1, diag2, vis, 0)
        # print(self.ans)
        return self.ans



            




n = 4
obj = Solution().totalNQueens(n)
print(obj)


