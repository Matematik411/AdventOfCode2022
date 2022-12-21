import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

file = [line.split(",") for line in file]

file = set(
    (int(x[0]), int(x[1]), int(x[2]))
    for x in file
    )
surface = len(file) * 6

X = [100, 0]
Y = [100, 0]
Z = [100, 0]


for cube in file:
    X[0] = min(cube[0], X[0])
    Y[0] = min(cube[1], Y[0])
    Z[0] = min(cube[2], Z[0])
    X[1] = max(cube[0], X[1])
    Y[1] = max(cube[1], Y[1])
    Z[1] = max(cube[2], Z[1])
    
    for dir in range(3):
        for d in [-1, 1]:
            n = list(cube)
            n[dir] += d

            n = tuple(n)

            if n in file:
                surface -= 1

print("a: ", surface)


# for b) find the outside area and count how many sides does it touch
outside = set()
outside_surface = 0

q = [(X[0]-1, Y[0]-1, Z[0]-1)]

while q:
    c = q.pop()

    if c in outside:
        continue
    outside.add(c)
    for dir in range(3):
        for d in [-1, 1]:
            n = list(c)
            n[dir] += d
            n = tuple(n)

            if n in file:
                outside_surface += 1
            
            elif (n not in outside) and (X[0] - 1 <= n[0] <= X[1] + 1) and (Y[0] - 1 <= n[1] <= Y[1] + 1) and (Z[0] - 1 <= n[2] <= Z[1] + 1):
                q.append(n)


print("b: ", outside_surface)
