import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()


w = len(file[0])
h = len(file)

grid = []

for line in file:
    row = [int(x) for x in line]
    grid.append(row)


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visible = 2 * w + 2 * (h-2)
max_scenic = 0

for j in range(1, h-1):
    for i in range(1, w-1):
        number = grid[j][i]
        add = False
        sight_score = 1

        for way in dirs:
            checking = [j, i]

            seen = True
            sight = 0
            while min(checking) > 0 and checking[0] < (h-1) and checking[1] < (w-1):
                checking[0] += way[0]
                checking[1] += way[1]

                sight += 1

                if grid[checking[0]][checking[1]] >= number:
                    seen = False
                    break 
            
            sight_score *= sight
            if seen:
                add = True
        
        if add:
            visible += 1
            max_scenic = max(max_scenic, sight_score)

print("a: ", visible)
print("b: ", max_scenic)
