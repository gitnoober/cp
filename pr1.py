class Solution:
    def isValidSudoku(self, board) -> bool:
        def check(i, j):
            return False if board[i][j] == "." else True

        n, ok = 9, True
        for i in range(n):
            vis, vis2 = [0] * 10, [0] * 10
            for j in range(n):
                if check(i, j):
                    vis[int(board[i][j])] += 1
                    if vis[int(board[i][j])] > 1:
                        ok = False

                if check(j, i):
                    vis2[int(board[j][i])] += 1
                    if vis2[int(board[j][i])] > 1:
                        ok = False

                if i % 3 == j % 3 == 0:
                    vis3 = [0] * 10
                    for k in range(i, i + 3):
                        for f in range(j, j + 3):
                            if not check(k, f):
                                continue
                            vis3[int(board[k][f])] += 1
                            if vis3[int(board[k][f])] > 1:
                                ok = False
        return ok


nums = [
    [".", "4", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "1", ".", ".", "7", ".", "."],
]


obj = Solution().isValidSudoku(nums)
# print(obj)

# 5000+ dollars
# 53 dollars
