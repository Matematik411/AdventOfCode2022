import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

total_str = 0
check = [20 + 40*i for i in range(6)]

cycle = 0
i = 0
reg = 1

crt = [[] for _ in range(6)]

while cycle < 240-1:
    instr = file[i]

    i += 1
    k = 0
    change = 1
    if instr != "noop":
        k = int(instr.split()[1])
        change = 2

    for _ in range(change):
        # b)
        # b uses positions which start counting at 0, so I only later increase the cycle index        
        if cycle % 40 in [reg-1, reg, reg+1]:
            crt[cycle // 40].append("#")
        else:
            crt[cycle // 40].append(".")

        # a)
        cycle += 1
        if cycle in check:
            total_str += cycle * reg

    reg += k

print("a: ", total_str)
print("b:")
for line in crt:
    print("".join(line))
