import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

h = len(file)
w = len(file[0])

# I outline the grid with characters higher than the field, we the path never goes there
grid = [["ž" for _ in range(w+2)]]
for row in file:
    grid.append(["ž"] + [x for x in row] + ["ž"])
grid.append(["ž" for _ in range(w+2)])

for j in range(len(grid)):
    for i in range(len(grid[0])):
        if grid[j][i] == "S":
            grid[j][i] = "a"
            start = (j, i)
        if grid[j][i] == "E":
            grid[j][i] = "z"
            goal = (j, i)
        
dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

# b) initialized on the solution of part a)
min_walk = 412

for j_s in range(len(grid)):
    for i_s in range(len(grid[0])):
        if grid[j_s][i_s] == "a":
            
            visited = set()
            q = []
            q.append([0, (j_s, i_s)]) 
            while q:
                d, c = q.pop(0)

                if c == goal:
                    if (j_s, i_s) == start:
                        print("a: ", d)

                    min_walk = min(min_walk, d)
                    break

                if c in visited:
                    continue

                visited.add(c)

                for dir in dirs:
                    y_n = c[0] + dir[0]
                    x_n = c[1] + dir[1]

                    if ord(grid[y_n][x_n]) <= (ord(grid[c[0]][c[1]]) + 1): 
                        q.append((d+1, (y_n, x_n)))


print("b: ", min_walk)