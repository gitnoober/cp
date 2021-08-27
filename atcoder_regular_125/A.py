import sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def maps():return [int(i) for i in input().split()]


def sol1(s , t):
	j = cur_idx = ans = 0
	ok = True
	d = {}
	while j < m:
		if t[j] == s[cur_idx]:
			ans+=1
		else:
			if (cur_idx , t[j]) not in d:
				l , r =  cur_idx , cur_idx
				dis1 = dis2 = 0
				while r < n and s[r] == s[cur_idx]:
					r+=1
					dis1+=1
					r%=n

				while l > -1 and s[l] == s[cur_idx]:
					if l == 0 :
						l = n
					l-=1
					dis2+=1

				if l>=0 and r <n and s[r] == t[j] and s[l] == t[j]:
					if dis1 < dis2:
						ans+=dis1
						d[(cur_idx , t[j])] = (r , dis1)
						cur_idx  = r
					else:
						ans+=dis2
						d[(cur_idx , t[j])] = (l , dis2)
						cur_idx = l

				elif r < n and s[r] == t[j] :
					ans+=dis1
					d[(cur_idx , t[j])] = (r , dis1)
					cur_idx = r

				elif l >=0 and s[l] == t[j]:
					ans+=dis2
					d[(cur_idx , t[j])] = (l , dis2)
					cur_idx = l

				else:
					ok = False
					break
			else:
				cur_idx , dis = d[(cur_idx , t[j])]
				ans+=dis
			ans+=1
		j+=1
	return ans

def sol2():
	res = m
	idx = 0

	while s[idx] == s[0] and s[0] == s[-idx]:
		idx+=1

	for i in range(m-1):
		if t[i] != t[i+1]:
			res+=1

	print(res + idx - (s[0] == t[0])) #if s[0] == t[0] then first rotation is enough so subtract -1 when s[0] =t[0]


T = 1
for _ in range(T):
	n , m = maps()
	s = [*maps()]
	t = [*maps()]

	if len(set(t)) == 1 
		print(m) if s[0] == t[0] else print(-1)

	else:
		sol2()
