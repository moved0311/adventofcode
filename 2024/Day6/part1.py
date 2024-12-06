with open('input') as file:
	maps = []
	pos = None

	for r, line in enumerate(file.read().strip().split('\n')):
		row = list(line)
		for c in range(len(row)):
			if row[c] == '^':
				pos = [r, c]
		maps.append(row)

	ROW = len(maps)
	COL = len(maps[0])
	direction = '^'

	def nextDirection(d):
		if d == '^':
			return '>'
		elif d == '>':
			return 'v'
		elif d == 'v':
			return '<'
		else:
			return '^'

	while True:
		[r, c] = pos
		maps[r][c] = 'X'
		moves = {
			'^': [r - 1, c],
			'v': [r + 1, c],
			'>': [r, c + 1],
			'<': [r, c - 1]
		}
		[nr, nc] = moves[direction]
		
		if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
			break
		if maps[nr][nc] == '#':
			direction = nextDirection(direction)
		else:
			pos = [nr, nc]

	cnt = 0
	for row in maps:
		for c in row:
			if c == 'X':
				cnt += 1
	
	print(cnt)
	