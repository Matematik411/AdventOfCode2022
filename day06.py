import sys
file = sys.stdin.read().split("\n")
if file[-1] == "":
    file.pop()

data = file[0]

last4 = ""
last14 = ""
doneA = False

i = 1
for a in data:
    last4 += a
    last14 += a

    if len(last4) > 4:
        last4 = last4[1:]
    if len(last14) > 14:
        last14 = last14[1:]
    
    if len(set(last4)) == 4 and not doneA:
        print("a: ", i)
        doneA = True

    if len(set(last14)) == 14:
        print("b: ", i)
        break

    i += 1