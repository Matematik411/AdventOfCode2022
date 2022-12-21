import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

print(file)
