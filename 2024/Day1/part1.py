with open('input') as file:
	col1 = []
	col2 = []
	for line in file.read().strip().split('\n'):
		[left, right] = line.split()
		col1.append(int(left))
		col2.append(int(right))
	col1.sort()
	col2.sort()
	N = len(col1)
	total = 0
	for i in range(N):
		total += abs(col1[i] - col2[i])
	print(total)