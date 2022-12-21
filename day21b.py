import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()



def update(name):
    if isinstance(monkeys[name], int):
        return monkeys[name]
    
    elif name == "humn":
        return "humn"
    
    
    fst, snd, sign = monkeys[name]

    a = update(fst)
    b = update(snd)

    if isinstance(a, int) and isinstance(b, int):


        monkeys[name] = eval(
            str(monkeys[fst])
            + sign
            + str(monkeys[snd])
            )
        return monkeys[name]
    
    else:
        monkeys[name] = ("(" + 
            str(monkeys[fst])
            + sign
            + str(monkeys[snd])
            + ")"
        )
            
        return monkeys[name]


main_one = "root"

found = False
human = 1
 
monkeys = {}
for line in file:
    data = line.split()

    if data[0] == "humn:":
        a, b = data
        monkeys[a[:-1]] = "humn"

    elif data[0] == "root:":
        a, b, c, d = line.split()

        monkeys[a[:-1]] = (b, d, "==")

    elif len(data) == 2:
        a, b = data
        monkeys[a[:-1]] = int(b)

    else:
        a, b, c, d = line.split()

        monkeys[a[:-1]] = (b, d, c)


update(main_one)
print(monkeys[main_one])
# I then copy this into Mathematica's Solve and get
print("b: ", 3451534022348)



