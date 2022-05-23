class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        row, col = len(grid), len(grid[0])
        vis = set()
        a = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        cnt = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in vis:
                    stack = [(r, c)]
                    vis.add((r, c))
                    for x1, y1 in stack:
                        for dx, dy in a:
                            x, y = x1 + dx, y1 + dy
                            if x < row and y < col and x >= 0 and y >= 0 and grid[x][y] == '1' and (x, y) not in vis:
                                stack.append((x, y))
                                vis.add((x, y))
                    ok = True
                    for x1, y1 in stack:
                        if x1 == row or y1 == col:
                            continue
                        for dx, dy in a:
                            x, y = x1 + dx, y1 + dy
                            if x >= row or y >= col:
                                continue
                            if x < 0 or y < 0:
                                continue
                            if (x, y) in vis:
                                continue
                            # print(x, y, row, col)
                            if grid[x][y] == '1':
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        cnt += 1
                        # print(stack)
                    # print(ok)
        return cnt


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
obj = Solution()
x = obj.numIslands(grid)
print(x, "ans")
