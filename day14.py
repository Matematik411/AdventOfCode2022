import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

max_x = 0
min_x = 1000
max_y = 0

for row in file:
    points = row.split(" -> ")
    for coords in points:
        x, y = map(int, coords.split(","))
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)

left_edge = min_x - 150
w = max_x - left_edge + 150
h = max_y + 2

grid = [[0 for _ in range(w)] for _ in range(h)]
# add floor
grid.append([1 for _ in range(w)])

for row in file:
    points = row.split(" -> ")

    for i in range(len(points) - 1):
        x1, y1 = map(int, points[i].split(","))
        x1 -= left_edge
        x2, y2 = map(int, points[i+1].split(","))
        x2 -= left_edge
        
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                grid[y][x1] = 1
        else:
            for x in range(min(x1, x2), max(x1, x2)+1):
                grid[y1][x] = 1

start = [500-left_edge, 0]
grains = 0
fallen = False
full_tree = False

while not (fallen and full_tree):
    pos = [start[0], start[1]]
    while True:

        if pos[1] > max_y and not fallen:
            fallen = True
            print("a: ", grains)
  
        # down
        if grid[pos[1]+1][pos[0]] == 0:
            pos[1] += 1
        # down left
        elif grid[pos[1]+1][pos[0]-1] == 0:
            pos[0] -= 1
            pos[1] += 1
        # down right
        elif grid[pos[1]+1][pos[0]+1] == 0:
            pos[0] += 1
            pos[1] += 1
        # stops
        else:
            grid[pos[1]][pos[0]] = 2

            if pos == start:
                full_tree = True
                print("b: ", grains + 1)
            break

    grains += 1
