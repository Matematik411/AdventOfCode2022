import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

main_one = "root"




monkeys = {}
for line in file:
    data = line.split()
    if len(data) == 2:
        a, b = data
        monkeys[a[:-1]] = int(b)
    else:
        a, b, c, d = line.split()

        monkeys[a[:-1]] = (b, d, c)

def update(name):
    if isinstance(monkeys[name], int):
        return True
    
    fst, snd, sign = monkeys[name]

    update(fst)
    update(snd)

    monkeys[name] = eval(
        str(monkeys[fst])
        + sign
        + str(monkeys[snd])
        )
    return monkeys[name]


update(main_one)
print("a: ", int(monkeys[main_one]))
