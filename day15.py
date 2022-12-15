import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

target_y = 2000000
sensors = []
radius = []
beacons = []

for sensor in file:
    _, _, x, y, _, _, _, _, x_b, y_b = sensor.split()

    x = int(x[2:-1])
    y = int(y[2:-1])
    x_b = int(x_b[2:-1])
    y_b = int(y_b[2:])

    sensors.append((x, y))
    beacons.append((x_b, y_b))
    radius.append(abs(x-x_b) + abs(y-y_b))


def circle(a, b, r):
    points = []
    dx = 0
    dy = -r
    change = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

    for s in range(4):
        for _ in range(r):
            dx += change[s][0]
            dy += change[s][1]
            points.append((a+dx, b+dy))
    return points

cannot_contain = set()

for i in range(len(sensors)):
    x, y = sensors[i]
    dy = abs(target_y - y)
    
    if dy <= radius[i]:
        cannot_contain.add((x, target_y))

        for k in range(radius[i]-dy):
            cannot_contain.add((x+(k+1), target_y))
            cannot_contain.add((x-(k+1), target_y))

# there exist a beacon on target_y
cannot_contain.remove((4401794, 2000000))
print("a: ", len(cannot_contain))

# b) we check the circles on the distance r+1 of each sensor
for i in range(len(sensors)):
    x, y = sensors[i]
    r = radius[i]

    points_to_check = circle(x, y, r+1)

    for (u, v) in points_to_check:
        ok = True
        for j in range(len(sensors)):
            a, b = sensors[j]
            d = abs(u-a) + abs(v-b)

            if d <= radius[j] and u <= 4000000:
                ok = False
                break
        
        if ok:
            print("b: ", 4000000*u + v)
            break

    if ok:
        break
