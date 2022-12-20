import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

N = len(file)
factor = 811589153

for i in range(N):
    file[i] = int(file[i]) * factor


unmixed = [(file[x], x) for x in range(N)]

for _ in range(10):
    for i in range(N):
        loc = unmixed.index((file[i], i))
        a, _ = unmixed.pop(loc)
        new_loc = (loc + a) % (N-1)

        unmixed = unmixed[:new_loc] + [(a, i)] + unmixed[new_loc:]

numbers = [x[0] for x in unmixed]
coords = 0
start = numbers.index(0)

for k in range(1, 4):
    new_i = (k * 1000 + start) % N
    coords += numbers[new_i]

print("a: ", 8721)
print("b: ", coords)