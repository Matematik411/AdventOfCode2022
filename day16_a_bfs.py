import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()



valves = {}
graph = {}

for line in file:
    _, loc, _, _, rate, _, _, _, _, *paths = line.split()

    
    valves[loc] = int(rate[5:-1])
    graph[loc] = [x.replace(",", "") for x in paths]

non_empty = set()
reduced_graph = {}
for k,v in valves.items():
    if v != 0:
        non_empty.add(k)
        reduced_graph[k] = {}

non_zero = len(non_empty)

# only non zero vertices
for k in reduced_graph:

    # run bfs to find all
    visited = set()
    q = [(0,k)]

    while len(reduced_graph[k]) < (non_zero - 1):
        d, c = q.pop(0)

        if c in visited:
            continue

        if c in non_empty and c != k:
            reduced_graph[k][c] = d
    
        visited.add(c)

        for n in graph[c]:
            if n not in visited:
                q.append((d+1, n))


starting_dist = {}
visited = set()
q = [(0,"AA")]

while len(starting_dist) < (non_zero):
    d, c = q.pop(0)
    if c in visited:
        continue

    if c in non_empty:
        starting_dist[c] = d

    visited.add(c)

    for n in graph[c]:
        if n not in visited:
            q.append((d+1, n))

# print(reduced_graph)
# print(starting_dist)
# print(valves)

q = []
for a_n in starting_dist:
    q.append(
        (0, 30-starting_dist[a_n], a_n, set())
    )
# print(q)
max_released = 0

while q:
    # print(q) 
    s, t, loc, opened = q.pop(0)
   

    if t <= 1 or (len(opened) == non_zero):
        continue

    if loc not in opened:
        opened.add(loc)
        s += (t-1) * valves[loc]
        max_released = max(max_released, s)
        t -= 1

    for n in reduced_graph[loc]:
        if (t-reduced_graph[loc][n] >= 2) and (n not in opened):
            q.append((
                s,
                t-reduced_graph[loc][n], 
                n, 
                set(x for x in opened)
                ))

print(max_released)
