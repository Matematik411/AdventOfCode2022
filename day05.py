import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

stacks = [[] for _ in range(9)]

for line in file[:8]:
    for i in range(0, 9):
        chr = line[4*i+1]
        if chr != " ":
            stacks[i].append(chr)

for s in stacks:
    s.reverse()

for command in file[10:]:
    c = command.split()
    x, y, z = map(int, [c[1], c[3], c[5]])

    # # a)
    # for _ in range(x):
    #     if stacks[y-1]:
    #         crate = stacks[y-1].pop()
    #         stacks[z-1].append(crate)

    # b)
    pile = []
    for _ in range(x):
        if stacks[y-1]:
            crate = stacks[y-1].pop()
            pile.append(crate)
    pile.reverse()
    for crate in pile:
        stacks[z-1].append(crate)

print("a:  GRTSWNJHH")
print("b: ", "".join([s[-1] for s in stacks]))