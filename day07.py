from collections import defaultdict
import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()
limit = 100000

graph = defaultdict(lambda: [])
dirsize = defaultdict(lambda: 0)

current = "/"
path = ["/"]

for line in file:
    line = line.split()
    if line[0] == "$":
        if line[1] == "ls":
            pass
        elif line[2] == "..":
            path.pop()
            current = path[-1]
        elif line[2] == "/":
            current = "/"
            path = ["/"]
        else:
            current = line[2]
            path.append(current)
        
        # so we have all names for later loop
        if "-".join(path) not in graph:
            graph["-".join(path)] = []

    else:
        size, name = line

        if size != "dir":
            dirsize["-".join(path)] += int(size)
        else:
            graph["-".join(path)].append(name)
            
def size_of_dir(name):
    total = dirsize[name]
    for dir in graph[name]:
        total += size_of_dir(name + "-" + dir)
    return total

sum_of_small = 0
for name in graph:
    size = size_of_dir(name)
    if size <= limit:
        sum_of_small += size

print("a: ", sum_of_small)

# b)
total = 70000000
unused = total - size_of_dir("/")
we_need = 30000000

smallest = total
for name in graph:
    size = size_of_dir(name)
    if (we_need - unused) <= size < smallest:
        smallest = size

print("b: ", smallest)
