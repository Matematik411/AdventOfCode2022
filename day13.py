import sys
import functools
file = sys.stdin.read().split("\n\n")
if file[-1][-1] == "\n":
    file[-1] = file[-1][:-1]
pairs = [pair.split("\n") for pair in file]

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0
    
    elif isinstance(a, int):
        return compare([a], b)
    
    elif isinstance(b, int):
        return compare(a, [b])
    
    else:
        for i in range(min(len(a), len(b))):
            c = compare(a[i], b[i])
            if (c is not None) and c != 0:
                return c    
        
        if len(a) != len(b):
            if len(a) < len(b):
                return 1
            else:
                return -1

list_of_all = [[2], [6]]
correctly_paired = 0

for i, pair in enumerate(pairs):
    l, r = pair

    l = eval(l)
    r = eval(r)

    list_of_all.append(l)
    list_of_all.append(r)

    c = compare(l, r)
    if c == 1:
        correctly_paired += i+1

print("a: ", correctly_paired)

sorted = sorted(list_of_all, key=functools.cmp_to_key(compare))
sorted.reverse()

print("b: ", (sorted.index([2])+1) * (sorted.index([6])+1))
