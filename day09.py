import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

dirs = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}

def touch(a, b):
    return max(abs(a[0]-b[0]),abs(a[1]-b[1])) <= 1

for part in [0, 1]:
    size_of_snake = 10 if part else 2

    positions = [[0, 0] for _ in range(size_of_snake)]
    tail_locs = set()

    for steps in file:
        d, k = steps.split()
        k = int(k)

        for _ in range(k):
            positions[0][0] += dirs[d][0]
            positions[0][1] += dirs[d][1]

            for link in range(1, size_of_snake):
                fst = positions[link-1]
                snd = positions[link]

                if not touch(fst, snd):
                    hor = fst[0]-snd[0]
                    ver = fst[1]-snd[1]

                    if abs(hor) > 0:
                        snd[0] += hor//abs(hor)
                    if abs(ver) > 0:
                        snd[1] += ver//abs(ver)
                
                positions[link] = snd          

            tail_locs.add(tuple(positions[-1]))

    part_name = "b: " if part else "a: "
    print(part_name + str(len(tail_locs)))
