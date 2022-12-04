import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

full = 0
overlap = 0

for pair in file:
    a, b = pair.split(",")
    x, y = map(int, a.split("-"))
    z, w = map(int, b.split("-"))

    if x <= z and y >= w:
        full += 1
    elif x >= z and y <= w:
        full += 1

    for i in range(x, y+1):
        if i >= z and i <= w:
            overlap += 1
            break


print("a: ", full)
print("b: ", overlap)
