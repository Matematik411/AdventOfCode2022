import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

points_a = 0
points_b = 0

symbols = {"X": 1, "Y": 2, "Z": 3 }
# from the view of you : ABC
win = {"A": "Z", "B": "X", "C": "Y"}
same = {"A": "X", "B": "Y", "C": "Z"}
lose = {"A": "Y", "B": "Z", "C": "X"}

for pair in file:
    you, me = pair.split()
   
    # part a)
    points_a += symbols[me]

    if same[you] == me:
        points_a += 3
    elif lose[you] == me:
        points_a += 6

    # part b)
    if me == "X":
        me = win[you]
    elif me == "Y":
        points_b += 3
        me = same[you]
    else:
        points_b += 6
        me = lose[you]
    points_b += symbols[me]


print("a: ", points_a)
print("b: ", points_b)
