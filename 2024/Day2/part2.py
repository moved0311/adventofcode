with open('input') as file:
	cnt = 0
	def checkIsSafe(row):
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
		return good and (isIncrease or isDecrease)
	
	for line in file.read().strip().split('\n'):
		row = list(map(int, line.split(' ')))
		N = len(row)
		if checkIsSafe(row):
			cnt += 1
		else: 
			for i in range(N): # try remove one element
				newRow = row[0: i] + row[i + 1:]
				if checkIsSafe(newRow):
					cnt += 1
					break
	print(cnt)
		