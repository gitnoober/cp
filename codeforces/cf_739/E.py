import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]

from collections import defaultdict

def check(se , dic):
	for i in se:
		if not dic[i] and already[ord(i) - 97] == -1:
			already[ord(i) - 97] = 1
			return True
	return False

def check2(d,s2 , occ):
	for i in range(len(s2)):
		if d[s2[i]] != occ[i]:
			return False
	return True


def main():
	s = input()
	n = len(s)
	unique = set(s)
	if len(unique) == 1:
		print(s ,s[0])
		return
		
	global already
	already = [0]*26

	for i in unique:
		already[ord(i) - 97] = -1
	
	og = defaultdict(int)
	di = defaultdict(list)
	I = 0
	for i in s:
		og[i]+=1
		di[i].append(I)
		I+=1

	s2 = ''.join([i for i, j in sorted(di.items() , key= lambda x : x[1][-1]) ])
	ok = True
	occ = []
	for i in range(len(s2)):
		if og[s2[i]]%(i+1) :
			ok = False
			break
		else:
			occ.append(og[s2[i]]//(i+1))
	#if ch is occuring k times in t , and it is the ith removed character then it is occuring sk(occurence of ch in original s)*i = k
	#k has to be divisible by i, else answer doesn't exist

	if ok:
		s1 = ''
		i = 0
		d = defaultdict(int)
		for i in range(n):
			d[s[i]]+=1
			if check2(d, s2, occ):
				s1 = s[:i+1]
				break

		S = s1
		idx = i
		for i in s2:
			s1 = s1.replace(i, '')
			S+=s1
		if S == s:
			print(s[:idx+1] , s2)
		else:
			print(-1)
	
	else:
		print(-1)



if __name__ == '__main__':
	for _ in range(*maps()):
		main()
