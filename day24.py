import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

H = len(file) - 2
W = len(file[0]) - 2

blizzards = set()
walls = {(-2, 0), (H+1,W-1)}
for j in range(H+2):
    for i in range(W+2):
        if file[j][i] == "#":
            walls.add((j-1, i-1))
        elif file[j][i] == ">":
            blizzards.add((j-1, i-1, 0, 1))
        elif file[j][i] == "<":
            blizzards.add((j-1, i-1, 0, -1))
        elif file[j][i] == "v":
            blizzards.add((j-1, i-1, 1, 0))
        elif file[j][i] == "^":
            blizzards.add((j-1, i-1, -1, 0))
start = (-1, 0)
end = (H, W-1)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

time = 0
# remember all the possible positions at each time
me = {start}
other_targets = [(start, end), (end, start)]
goal = end

while True:
    time += 1
    new = {p for p in me}
    for d in dirs:
        new = new.union({(p[0]+d[0], p[1]+d[1]) for p in me})
    
    blizz_pos = {
        (
            (b[0] + time*b[2]) % H,
            (b[1] + time*b[3]) % W
        )
        for b in blizzards
    }
    moves = new - blizz_pos - walls
    if goal in moves:
        print("made it through", time)
        if other_targets:
            loc, target = other_targets.pop()
            goal = target
            me = {loc}
        else:
            break
    else:
        me = {p for p in moves}
    
