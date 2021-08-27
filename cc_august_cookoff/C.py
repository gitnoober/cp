import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]

from collections import defaultdict

result = []
def backtrack(nums, start, curr_set):
	
	# Global result
	result.append(list(curr_set))
	
	for i in range(start, len(nums)):
		if (i > start and nums[i] == nums[i - 1]):
			continue
		curr_set.append(nums[i])
		backtrack(nums, i + 1, curr_set)
		curr_set.pop()

def AllSubsets(nums):

	curr_set = []
	nums.sort()
	backtrack(nums, 0, curr_set)
	
def pr(a):
	pr = 1
	for i in a:
		pr*=i
	return pr

def naive(n , a):
	d = defaultdict(int)
	for i in a:
		d[i]+=1
	AllSubsets(a)

	# print(a, result,sep='\n')
	# print("ppp")
	ok = True
	for i in result:
		if len(i) and d[pr(i)] == 0:
			ok = False
			break
	result.clear()
	return ok


	
def main():
	# n, = maps()
	# a = [*maps()]
	if n == 1:
		return 1
	if n == 2:
		if a[0]*a[1] in a:
			return 1
		else:
			return 0
		
	posi , negi , neg1 , one = 0 , 0 , 0 ,0 
	for i in a:
		if i > 1 :
			posi+=1
		if i < -1:
			negi+=1
		if i == -1:
			neg1+=1
		if i == 1:
			one+=1

	if (posi + negi) == 0:
		if neg1 > 1 :
			if one == 0:
				return 0
			else:
				return 1
		else:
			return 1
	elif posi == 0 and negi== 1:
		if neg1 > 0 :
			return 0
		else:
			return 1

	elif posi == 1 and negi == 0 :
		if neg1 > 0 and one >0 :
			return 0
		elif neg1 == 0 :
			return 1
		else:
			return 0
	else:
		return 0


for _ in range(*maps()):
	n, = maps()
	a = [*maps()]
	ans1 = main()
	print(ans1)