import sys
from collections import defaultdict
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

elves = set()
for j in range(len(file)):
    for i in range(len(file[0])):
        if file[j][i] == "#":
            elves.add((j, i))

#         0         1       2       3       4       5          6        7
#         N         NE      E       SE      S       SW         W        NW
neigh = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
dirs = [(0, 1, 7), (4, 3, 5), (6, 7, 5), (2, 1, 3)]

round = 0
while True:
    moves_to = defaultdict(lambda: [])
    elves_moved = 0
    round += 1
    for elf in elves:
        y, x = elf

        n = [(1 if ((y+neigh[i][0], x+neigh[i][1]) in elves) else 0) for i in range(8)]

        elves_moved += 1
        if sum(n) == 0:
            # continue
            moves_to[(y, x)].append((y, x))
            elves_moved -= 1
        elif sum([n[dirs[0][k]] for k in range(3)]) == 0:
            moves_to[(y+neigh[dirs[0][0]][0], x+neigh[dirs[0][0]][1])].append((y, x))
        elif sum([n[dirs[1][k]] for k in range(3)]) == 0:
            moves_to[(y+neigh[dirs[1][0]][0], x+neigh[dirs[1][0]][1])].append((y, x))
        elif sum([n[dirs[2][k]] for k in range(3)]) == 0:
            moves_to[(y+neigh[dirs[2][0]][0], x+neigh[dirs[2][0]][1])].append((y, x))
        elif sum([n[dirs[3][k]] for k in range(3)]) == 0:
            moves_to[(y+neigh[dirs[3][0]][0], x+neigh[dirs[3][0]][1])].append((y, x))
        else:
            moves_to[(y, x)].append((y, x))
            elves_moved -= 1
        
    dirs = dirs[1:] + [dirs[0]]


    elves_new = set()
    for move, elves_to_move in moves_to.items():
        if len(elves_to_move) == 1:
            elves_new.add(move)
        else:
            for elf in elves_to_move:
                elves_new.add(elf)

    elves = elves_new
    if elves_moved == 0:
        print("b: ", round)
        break

    if round == 10:
        X = [100, -100]
        Y = [100, -100]

        for elf in elves:
            y, x = elf
            X[0] = min(X[0], x)
            Y[0] = min(Y[0], y)
            X[1] = max(X[1], x)
            Y[1] = max(Y[1], y)

        empty = 0

        for j in range(Y[0], Y[1]+1):
            for i in range(X[0], X[1]+1):
                if (j, i) not in elves:
                    empty += 1

        print("a: ", empty)