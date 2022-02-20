def calc_mex(a):
	ok = [False]*1000
	n = len(a)
	prmx, sfmx = [] , []
	mx1, mx2 = 0,0
	i = 0
	while i < n :
		if a[i] < 1000:
			ok[a[i]] = True
			while ok[mx1]:
				mx1+=1
		i+=1
		prmx.append(mx1)

	mx1 = 0
	ok = [False]*1000
	i = n-1
	while i > -1 :
		if a[i] < 1000:
			ok[a[i]] = True
			while ok[mx1]:
				mx1+=1
		i-=1
		sfmx.append(mx1)

	sfmx = sfmx[::-1]
	ans = 0
	for i in range(len(a)-1):
		ans = max(ans, prmx[i]+sfmx[i+1])
	return ans

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	ANS = 0
	for i in range(n):
		for j in range(i+1,n+1):
			# print(a[i:j])
			arr = a[i:j]
			if len(arr) == 1 :
				if arr[0] == 0 :
					ANS+=2
				else:
					ANS+=1
			else:
				ANS += max(calc_mex(a[i:j]) + 2, len(a[i:j]) + a[i:j].count(0))
				# print(a[i:j], calc_mex(a[i:j]), len(a[i:j]) )
	print(ANS)

