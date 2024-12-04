from collections import defaultdict

with open('input2') as file:
    words = []
    for line in file.read().strip().split('\n'):
        words.append(list(line))

    ROW = len(words)
    COL = len(words[0])
    times = 0
    for r in range(ROW):
        for c in range(COL):
            if words[r][c] == 'A':
                directions = [
                    (r - 1, c - 1),
                    (r + 1, c - 1),
                    (r - 1, c + 1),
                    (r + 1, c + 1)
                ]
                cnt = defaultdict(int)
                pos_m = []

                for (nr, nc) in directions:
                    if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                        break
                    cnt[words[nr][nc]] += 1
                    if words[nr][nc] == 'M':
                        pos_m.append((nr, nc))

                if cnt['M'] == 2 and cnt['S'] == 2:
                    [[x_m1, y_m1], [x_m2, y_m2]] = pos_m
                    bad = (x_m1 != x_m2 and y_m1 != y_m2)
                    # M S
                    #  A
                    # S M (bad)
                    if not bad:
                        times += 1

    print(times)
