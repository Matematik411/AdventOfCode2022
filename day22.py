import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

movement = file.pop()
file.pop()

loc = [
    0,
    file[0].index(".")
]

# E S W N
# 0 1 2 3
step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
facing = 0


def opposite(y, x, looking):
    while file[y][x] != " ":
        y += step[(looking+2)%4][0]
        x += step[(looking+2)%4][1]

        if (0 > y) or (y >= len(file)) or (0 > x) or (x >= len(file[y])):
            break
    y -= step[(looking+2)%4][0]
    x -= step[(looking+2)%4][1]

    return y, x

def opposite_cube(y, x, looking):
    # area 1
    if (100 <= y < 150) and (50 <= x < 100):
        if looking == 0:
            Y = 49 - (y - 100)
            X = 149
            dir = 2
        elif looking == 1:
            Y = 150 + (x - 50)
            X = 49
            dir = 2
    # area 2
    elif (100 <= y < 150) and (0 <= x < 50):
        if looking == 2:
            Y = 49 - (y - 100)
            X = 50
            dir = 0
        elif looking == 3:
            Y = 50 + (x - 0)
            X = 50
            dir = 0
    # area 3
    elif (150 <= y < 200) and (0 <= x < 50):
        if looking == 0:
            Y = 149
            X = 50 + (y - 150)
            dir = 3
        elif looking == 1:
            Y = 0
            X = 100 + (x - 0)
            dir = 1
        elif looking == 2:
            Y = 0
            X = 50 + (y - 150)
            dir = 1
    # area 4
    elif (0 <= y < 50) and (100 <= x < 150):
        if looking == 0:
            Y = 149 - (y - 0)
            X = 99
            dir = 2
        elif looking == 1:
            Y = 50 + (x - 100)
            X = 99
            dir = 2
        elif looking == 3:
            Y = 199
            X = 0 + (x - 100)
            dir = 3
    # area 5
    elif (50 <= y < 100) and (50 <= x < 100):
        if looking == 0:
            Y = 49
            X = 100 + (y - 50)
            dir = 3
        elif looking == 2:
            Y = 100
            X = 0 + (y - 50)
            dir = 1
    # area 6
    elif (0 <= y < 50) and (50 <= x < 100):
        if looking == 2:
            Y = 149 - (y - 0)
            X = 0
            dir = 0
        elif looking == 3:
            Y = 150 + (x - 50)
            X = 0
            dir = 0

    return (Y, X, dir)

i_m = 0
steps = ""
while i_m < len(movement):

    if movement[i_m] not in "LR":
        steps += movement[i_m]
        i_m += 1
        continue

    for _ in range(int(steps)):
        y_n = loc[0] + step[facing][0]
        x_n = loc[1] + step[facing][1]

        if (y_n >= len(file)) or (y_n < 0) or (x_n < 0) or (x_n >= len(file[y_n])) or (file[y_n][x_n] == " "):
            # loop around
            # # a)
            # y_op, x_op = opposite(loc[0], loc[1], facing)
            # b)
            y_op, x_op, new_dir = opposite_cube(loc[0], loc[1], facing)

            if file[y_op][x_op] == "#":
                break

            loc = [y_op, x_op]
            facing = new_dir
            continue
        
        if file[y_n][x_n] == "#":
            break
        loc = [y_n, x_n]
  
    if movement[i_m] == "L":
        facing = (facing - 1) % 4
    elif movement[i_m] == "R":
        facing = (facing + 1) % 4

    steps = ""
    i_m += 1

# last steps ---------------
for _ in range(int(steps)):
    y_n = loc[0] + step[facing][0]
    x_n = loc[1] + step[facing][1]

    if (y_n >= len(file)) or (y_n < 0) or (x_n < 0) or (x_n >= len(file[y_n])) or (file[y_n][x_n] == " "):
        # loop around
        # # a)
        # y_op, x_op = opposite(loc[0], loc[1], facing)
        # b)
        y_op, x_op, new_dir = opposite_cube(loc[0], loc[1], facing)

        if file[y_op][x_op] == "#":
            break

        loc = [y_op, x_op]
        facing = new_dir
        continue
    
    if file[y_n][x_n] == "#":
        break
    loc = [y_n, x_n]
# ------------

print("a: ", 77318)
print("b: ", 1000 * (loc[0]+1) + 4 * (loc[1]+1) + facing)
