import sys
file = sys.stdin.read().split("\n")
file = file[0]

def nice_print(grid):
    for row in grid:
        print("".join(row))
    print()

pieces = [
    # ..@@@@.
    (1, [[0, 3], [0, 4], [0, 5], [0, 6]]),
    # ...@...
    # ..@@@..
    # ...@...
    (3, [[2, 4], [1, 3], [1, 4], [1, 5], [0, 4]]),
    # ....@..
    # ....@..
    # ..@@@..
    (3, [[2, 3], [2, 4], [2, 5], [1, 5], [0, 5]]),
    # ..@....
    # ..@....
    # ..@....
    # ..@....
    (4, [[3, 3], [2, 3], [1, 3], [0, 3]]),
    # ..@@...
    # ..@@...
    (2, [[1, 3], [1, 4], [0, 3], [0, 4]])
]
blank_line = ["|"] + ["."] * 7 + ["|"]
chamber = [[p for p in blank_line] for _ in range(3)]
chamber.append(["+"] + ["-"] * 7 + ["+"])


high_point = 0
piece_nr = 0
wind = 0
N = len(file)
P = len(pieces)
H = 3

h_changes = []
LOOP_AT = 0

for r in range(5000):
    h, piece = pieces[piece_nr]
    piece_nr = (piece_nr + 1) % P
    chamber = [[p for p in blank_line] for _ in range(h)] + chamber
    H += h

    while True:
        dx = -1 if file[wind] == "<" else 1
        wind = (wind + 1) % N

        on_side = set(
            chamber[p[0]][p[1]+dx] for p in piece
        )
        if on_side == {"."}:
            piece = [[p[0], p[1]+dx] for p in piece]
        
        below = set(
            chamber[p[0]+1][p[1]] for p in piece
        )
        if below == {"."}:
            piece = [[p[0]+1, p[1]] for p in piece]
        else:
            break

    for p in piece:
        chamber[p[0]][p[1]] = "#"
    new_peak = max(H - min(p[0] for p in piece), high_point)
    h_changes.append(new_peak-high_point)
    high_point = new_peak
    for _ in range(H - (high_point+3)):
        chamber = chamber[1:]
        H -= 1
    
    if r > 500:
        last_100 = h_changes[-100:]
        for i in range(r-100):
            sample = h_changes[i:i+100]
            if sample == last_100:
                print("FOUND IT !!!!", r, i)
                LOOP_AT = r

    if LOOP_AT:
        break
    
# nice_print(chamber)
# nice_print(image)
print("a: ", 3202)
# print(h_changes)
print("check if loop is aligned")
print(h_changes[229:229+15])
print(h_changes[1974:1974+15])
loop_len = 1974-229

starting = h_changes[:229]
loop = h_changes[229:1974]


total_dropped = 1000000000000
nr_of_loops = (total_dropped - 229) // len(loop)
remainder = (total_dropped - 229) % len(loop)

remainder_changes = loop[:remainder]

total_height = sum(starting) + sum(loop) * nr_of_loops + sum(remainder_changes)


print("b: ", total_height)