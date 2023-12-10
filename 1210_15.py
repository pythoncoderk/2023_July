k, g, m = map(int, input().split())
# print(k, g, m)
g2 = g
m2 = m
for i in range(k):
    if g2 == g:
        g2 = 0
    elif m2 == 0:
        m2 = m
    else:
        if g - g2 < m2:
            x = g - g2
            m2 -= x
            g2 += x
        elif g - g2 == m2:
            x = g - g2
            m2 -= x
            g2 += x
        else:
            x = m2
            m2 -= x
            g2 += x
print(g2, m2)

