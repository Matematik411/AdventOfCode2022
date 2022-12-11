import sys
file = sys.stdin.read().split("\n\n")
if file[-1] == "":
    file.pop()

rules = []
for monkey in file:
    rule = []
    
    lines = monkey.split("\n")

    starting = lines[1].split(": ")[1]
    rule.append(list(map(int, starting.split(", "))))

    operation = lines[2].split(": ")[1]
    rule.append(operation)

    test = lines[3].split()[-1]
    rule.append(int(test))

    true = lines[4].split()[-1]
    rule.append(int(true))

    false = lines[5].split()[-1]
    rule.append(int(false))

    rules.append(rule)

monkeys = [monkey[0] for monkey in rules]

nr_of_throws = [0 for _ in range(len(rules))]

# factor for part b)
factor = 1
for monkey in rules:
    factor *= monkey[2]

for round in range(10000):

    for m in range(len(rules)):

        for item in monkeys[m]:
            nr_of_throws[m] += 1

            _, _, a, b, c = rules[m][1].split()

            if c == "old":
                c = item
            else:
                c = int(c)

            if b == "+":
                new = item + c
            else:
                new = item * c

            # # a) used division by 3 here
            # new //= 3

            # in b) we don't divide, but we can only take the remainder by the lcm (simply their product) of all the monkeys' tests
            new %= factor

            test = (new % rules[m][2] == 0)

            if test:
                monkeys[rules[m][3]].append(new)
            else:
                monkeys[rules[m][4]].append(new)
            
        monkeys[m] = []
    
# a)
print("a:  110264")

nr_of_throws.sort()
print("b: ", nr_of_throws[-1] * nr_of_throws[-2])
