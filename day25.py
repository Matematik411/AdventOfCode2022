import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

sum = 0
for number in file:
    base = 0
    for x in number[::-1]:
        if x in ["0", "1", "2"]:
            sum += (5**base) * int(x)
        elif x == "-":
            sum += (5**base) * (-1)
        else:
            sum += (5**base) * (-2)
        base += 1

output = ""
while sum > 0:

    rem = sum % 5

    if rem in [0, 1, 2]:
        output = str(rem) + output
    elif rem == 4:
        output = "-" + output
        sum += 1
    elif rem == 3:
        output = "=" + output
        sum += 2

    sum //= 5

print("a: ", output)
