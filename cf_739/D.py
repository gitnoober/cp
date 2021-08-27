import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]

def calc(s1,s2):
	if word1 == word2:
		return 0
	#convert s1 to s2
	n1 , n2 = len(word1) , len(word2)
	i = dele = common = j =0
	while j < n1 and i < n2:
		if word2[i] == word1[j]:
			j+=1
			common+=1
			i+=1
		else:
			j+=1

	return (n1 - common) + dele + (n2 - i)


arr = []
for i in range(60):
	arr.append(str(1<<i))

ok = False
for _ in range(*maps()):
	n = input()
	ans = n+1
	for i in range(60):
		ans = min(ans, calc(n, arr[i]))

	print(ans)
