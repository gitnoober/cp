import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]

def fu():

	n , = maps()
	pr_arr = [1]*10
	pr = 1
	while pr < n :
		idx = pr_arr.index(min(pr_arr))
		pr/=pr_arr[idx]
		pr_arr[idx]+=1
		pr*=pr_arr[idx]

	t = list('codeforces')
	[print(pr_arr[i]*t[i] , end= '') for i in range(10)]

