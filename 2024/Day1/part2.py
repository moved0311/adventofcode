from collections import Counter

with open('input') as file:
	col1 = []
	col2 = []
	for line in file.read().strip().split('\n'):
		[left, right] = line.split()
		col1.append(int(left))
		col2.append(int(right))
	
	N = len(col1)
	cnt = Counter(col2)
	total = 0

	for i in range(N):
		total += col1[i] * cnt[col1[i]]
	print(total)