from collections import defaultdict
import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

# a)
repeats = 0
for sack in file:
    n = len(sack)
    first_half = set(sack[:n//2])

    item = first_half.intersection(sack[n//2:]).pop()

    if item in first_half:
        if ord(item) - ord("a") + 1 < 0:
            repeats += ord(item) - ord("A") + 1 + 26
        else:
            repeats += ord(item) - ord("a") + 1
print("a: ", repeats)

# b)
badges = 0
for i in range(len(file) // 3):
    a = file[3*i]
    b = file[3*i+1]
    c = file[3*i+2]

    badge = set(a).intersection(set(b)).intersection(set(c)).pop()

    if ord(badge) - ord("a") + 1 < 0:
        badges += ord(badge) - ord("A") + 1 + 26
    else:
        badges += ord(badge) - ord("a") + 1

print("b: ", badges)
