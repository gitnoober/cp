from collections import defaultdict

def check(arr, i , j):
	dxdy = [(-1,1), (1,-1),(-1,-1),(1,1)]
	n, cnt = 8, 0
	for dx,dy in dxdy:
		x,y = i + dx, j +dy
		if x >= 0 and x < n-1 and y >=0 and y < n - 1:
			if arr[x][y] == "#":
				cnt+=1
			else:
				return False
	if cnt > 1 :
		return True

	return False

def all_d(arr, i ,j):
	dxdy = [(-1,1), (1,-1)]
	st = [(i,j)]
	vis = {(i,j)}
	n = 8

	for ii,jj in st:
		for dx,dy in dxdy:
			x,y = dx+ii, dy+jj
			if x >= 0 and x < n - 1 and y >=0 and y < n - 1 and arr[x][y] == "#" and (x,y) not in vis:
				vis.add((x,y))
				st.append((x,y))
	return vis	


for _ in range(int(input())):
	input()

	arr = []
	n = 8
	for i in range(n):
		arr.append([j for j in input()])

	dxdy = [(-1,1), (1,-1)]
	ok = False

	for i in range(1,n-1):
		for j in range(1,n-1):
			if arr[i][j] == "#":
				if arr[i-1][j-1] == arr[i+1][j+1] == arr[i+1][j-1] == arr[i-1][j+1] == "#":
					print(i+1,j+1)
					ok = True

			if ok :
				break

		if ok :
			break
	if not ok :

		c = [(0,0),(0,n-1), (n-1,0),(n-1,n-1)]

		for i,j in c :
			if arr[i][j] == "#":
				print(i+1,j+1)
				break
				




	











