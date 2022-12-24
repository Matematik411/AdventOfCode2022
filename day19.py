import sys
from functools import lru_cache
import math
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

robots = []

for line in file:
    s = line.split()
    values = tuple(map(int, [s[6], s[12], s[18], s[21], s[27], s[30]]))
    robots.append(values)


best_result = 0
@lru_cache(maxsize=None)
def mining(t, dr, mi, rob):
    global best_result
    if t == 0:
        return mi[3]
    
    if t == 1:
        return mi[3] + dr[3]

    if t == 2:
        if (mi[0] >= rob[4]) and (mi[2] >= rob[5]):
            return mi[3] + dr[3] * 2 + 1
        else:
            return mi[3] + dr[3] * 2


    upper = mi[3]
    for k in range(t):
        upper += dr[3] + k
    if upper <= best_result:
        return 0

    ad_mi = tuple(
        mi[i] + dr[i] for i in range(4)
    )

    most_geodes = mi[3] + dr[3] * t
    # build geode drill
    if (mi[0] >= rob[4]) and (mi[2] >= rob[5]):
        return mining(
                t - 1, 
                (dr[0], dr[1], dr[2], dr[3] + 1),
                (
                    mi[0] + dr[0] - rob[4], 
                    mi[1] + dr[1], 
                    mi[2] + dr[2] - rob[5], 
                    mi[3] + dr[3]
                ),
                rob
            )
    elif (dr[0] > 0) and (dr[2] > 0):
        # if we have both mines we jump to the build time of geode drill
        dt = math.ceil(max(
            (rob[4] - mi[0]) / dr[0],
            (rob[5] - mi[2]) / dr[2]
        ))
        if t - (dt+1) > 0:
            most_geodes = max(
                most_geodes,
                mining(
                    t - dt - 1,
                    (dr[0], dr[1], dr[2], dr[3] + 1),
                    (
                        mi[0] + (dt+1) * dr[0] - rob[4],
                        mi[1] + (dt+1) * dr[1],
                        mi[2] + (dt+1) * dr[2] - rob[5],
                        mi[3] + (dt+1) * dr[3]
                    ),
                    rob
                )
            )

    # build obsidian drill
    if (mi[0] >= rob[2]) and (mi[1] >= rob[3]):
        most_geodes = max(
            most_geodes,
            mining(
                t - 1, 
                (dr[0], dr[1], dr[2] + 1, dr[3]),
                (
                    mi[0] + dr[0] - rob[2], 
                    mi[1] + dr[1] - rob[3], 
                    mi[2] + dr[2], 
                    mi[3] + dr[3]
                ),
                rob
            ))
    elif (dr[0] > 0) and (dr[1] > 0):
        # if we have both mines we jump to the build time of geode drill
        dt = math.ceil(max(
            (rob[2] - mi[0]) / dr[0],
            (rob[3] - mi[1]) / dr[1]
        ))
        if t - (dt+1) > 2: # the robot must have time to have some effect or we won't build it
            most_geodes = max(
                most_geodes,
                mining(
                    t - dt - 1,
                    (dr[0], dr[1], dr[2] + 1, dr[3]),
                    (
                        mi[0] + (dt+1) * dr[0] - rob[2],
                        mi[1] + (dt+1) * dr[1] - rob[3],
                        mi[2] + (dt+1) * dr[2],
                        mi[3] + (dt+1) * dr[3]
                    ),
                    rob
                )
            )

    # build clay drill
    if (mi[0] >= rob[1]):
        most_geodes = max(
            most_geodes,
            mining(
                t - 1, 
                (dr[0], dr[1] + 1, dr[2], dr[3]),
                (
                    mi[0] + dr[0] - rob[1], 
                    mi[1] + dr[1], 
                    mi[2] + dr[2], 
                    mi[3] + dr[3]
                ),
                rob
            ))
    elif (dr[0] > 0):
        # if we have both mines we jump to the build time of geode drill
        dt = math.ceil(
            (rob[1] - mi[0]) / dr[0]
        )
        if t - (dt+1) > 2: # the robot must have time to have some effect or we won't build it
            most_geodes = max(
                most_geodes,
                mining(
                    t - dt - 1,
                    (dr[0], dr[1] + 1, dr[2], dr[3]),
                    (
                        mi[0] + (dt+1) * dr[0] - rob[1],
                        mi[1] + (dt+1) * dr[1],
                        mi[2] + (dt+1) * dr[2],
                        mi[3] + (dt+1) * dr[3]
                    ),
                    rob
                )
            )

    # build ore drill
    if dr[0] < max([rob[0], rob[1], rob[2], rob[4]]):
        if (mi[0] >= rob[0]):
            most_geodes = max(
                most_geodes,
                mining(
                    t - 1, 
                    (dr[0] + 1, dr[1], dr[2], dr[3]),
                    (
                        mi[0] + dr[0] - rob[0], 
                        mi[1] + dr[1], 
                        mi[2] + dr[2], 
                        mi[3] + dr[3]
                    ),
                    rob
                ))
        elif (dr[0] > 0):
            # if we have both mines we jump to the build time of geode drill
            dt = math.ceil(
                (rob[0] - mi[0]) / dr[0]
            )
            if t - (dt+1) > 2: # the robot must have time to have some effect or we won't build it
                most_geodes = max(
                    most_geodes,
                    mining(
                        t - dt - 1,
                        (dr[0] + 1, dr[1], dr[2], dr[3]),
                        (
                            mi[0] + (dt+1) * dr[0] - rob[0],
                            mi[1] + (dt+1) * dr[1],
                            mi[2] + (dt+1) * dr[2],
                            mi[3] + (dt+1) * dr[3]
                        ),
                        rob
                    )
                )

    best_result = max(best_result, most_geodes)
    return most_geodes
    
result = 0
for k, robot in enumerate(robots):
    best_result = 0
    a = mining(24, (1, 0, 0, 0), (0, 0, 0, 0), robot)
    result += a * (k+1)
    mining.cache_clear()

print("a: ", result)

result = 1
for robot in robots[:3]:
    best_result = 0
    a = mining(32, (1, 0, 0, 0), (0, 0, 0, 0), robot)
    result *= a 
    mining.cache_clear()
print("b: ", result)