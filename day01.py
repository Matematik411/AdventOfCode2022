import sys
file = sys.stdin.read().split("\n")

c = 0
m_a = 0
m_b = [0, 0, 0]


for e in file:
    
    if e != "":
        c += int(e)

    
    if e == "":
        # a)
        if c > m_a:
            m_a = c
        # b)
        if c > m_b[-1]:
            m_b.append(c)
            m_b.sort(reverse=True)
            m_b.pop()
        c = 0

print("a: ", m_a)
print("b: ", sum(m_b))