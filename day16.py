import sys
from functools import lru_cache
import itertools
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


# --------------------------------
# solution from here, i now have everything needed prepared

@lru_cache(maxsize=None)
def walk(t, loc, remaining):
    best = 0

    for i in range(len(remaining)//2):
        room = remaining[2*i:2*i+2]
        others = remaining[:2*i] + remaining[2*i+2:]
        if (t-1) > reduced_graph[loc][room]:
            best = max(
                best,
                walk(
                    t-reduced_graph[loc][room]-1, 
                    room, 
                    others
                )
            )
    return best + (t-1) * valves[loc]

# part a) -> only 1 person walking around
best_choice = 0
for starting in starting_dist:
    others = "".join([y for y in non_empty if y != starting])

    choice = walk(
        30-starting_dist[starting],
        starting, 
        others)
    best_choice = max(best_choice, choice)
print("a: ", best_choice)


# part b)
# i split the non_empty set into 2 parts
total_best = 0
for size in range(2, 8):
    print(size)
    for my_rooms in itertools.combinations(non_empty, size):
        my_best = 0
        for starting in my_rooms:
            others = "".join([y for y in my_rooms if y != starting])

            choice = walk(
                26-starting_dist[starting],
                starting, 
                others)
            my_best = max(my_best, choice)
        
        elephant_rooms = [x for x in non_empty if x not in my_rooms]
        el_best = 0
        for starting in elephant_rooms:
            others = "".join([y for y in elephant_rooms if y != starting])

            choice = walk(
                26-starting_dist[starting],
                starting, 
                others)
            el_best = max(el_best, choice)

        total_best = max(total_best, my_best + el_best)

print("b: ", total_best)