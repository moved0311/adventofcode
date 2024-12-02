with open('input') as file:
	cnt = 0
	for line in file.read().strip().split('\n'):
		row = list(map(int, line.split(' ')))
		N = len(row)
		good = True
		isIncrease = True
		isDecrease = True
		for i in range(N - 1):
			if (row[i] <= row[i + 1]):
				isDecrease = False
			if (row[i] >= row[i + 1]):
				isIncrease = False			
			if abs(row[i] - row[i + 1]) > 3:
				good = False
				break
		if good and (isIncrease or isDecrease):
			cnt += 1
	print(cnt)
		