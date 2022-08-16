def YES():
    print("YES")


def NO():
    print("NO")


def main():

    for _ in range(int(input())):
        n, m = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(n)]
        if n == m == 1:
            YES() if arr[0][0] == 0 else NO()
            continue

        ok = False
        st = [(n - 1, m - 1, arr[-1][-1])]
        vis = {(n - 1, m - 1, arr[n - 1][m - 1])}
        dxdy = [(-1, 0), (0, -1)]

        for r, c, d in st:
            if r == 0 and c == 0 and d == 0:
                ok = True
                break

            for dx, dy in dxdy:
                rr, cc = r + dx, c + dy
                if rr < 0 or cc < 0 or rr >= n or cc >= m:
                    continue

                dd = d + arr[rr][cc]
                if (rr, cc, dd) in vis:
                    continue

                if dd + (n - rr) + (m - cc) < 0:
                    continue

                st.append((rr, cc, dd))
                vis.add((rr, cc, dd))

        YES() if ok else NO()


if __name__ == "__main__":
    main()
