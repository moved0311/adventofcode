with open('input') as file:
    words = []
    for line in file.read().strip().split('\n'):
        words.append(list(line))

    ROW = len(words)
    COL = len(words[0])
    MAS = 'MAS'
    times = 0
    for r in range(ROW):
        for c in range(COL):
            if words[r][c] == 'X':
                directions = [
                    [(r - 1, c), (r - 2, c), (r - 3, c)], # top
                    [(r + 1, c), (r + 2, c), (r + 3, c)], # down
                    [(r, c + 1), (r, c + 2), (r, c + 3)], # right
                    [(r, c - 1), (r, c - 2), (r, c - 3)], # left
                    [(r - 1, c + 1), (r - 2, c + 2), (r - 3, c + 3)], # top-right
                    [(r - 1, c - 1), (r - 2, c - 2), (r - 3, c - 3)], # top-left
                    [(r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3)], # down-right
                    [(r + 1, c - 1), (r + 2, c - 2), (r + 3, c - 3)], # down-left
                ]
                for direction in directions:
                    good = True
                    for i, (nr, nc) in enumerate(direction):
                        if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or words[nr][nc] != MAS[i]:
                            good = False
                            break
                    if good:
                        times += 1
    print(times)
