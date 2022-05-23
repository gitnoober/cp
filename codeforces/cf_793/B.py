for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = sorted(a)
	idx = 0
	ok = True
	arr = [ ]
	for i in range(n):
		if a[i] != b[i]:
			# print(b[i])
			# idx = i
			# ok = False
			# break
		# if not ok :
			arr.append((a[i], b[i]))

	# print(arr)
	# print(arr[0])
	res = arr[0][0] & arr[0][1]
	for j in range(1, len(arr)):
		res &= arr[j][0] & arr[j][1]
	print(res)


	# res = a[idx]
	# print(idx, "idx", res)
	# for j in range(idx+1,n):
	# 	res&=b[j]
	# print(res)
