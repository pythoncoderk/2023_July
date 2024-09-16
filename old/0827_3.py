n = int(input())

for i in range(n):
    x = list(input().split())
    h = int(x[0][:2])
    m = int(x[0][3:])
    h_1 = int(x[1])
    m_1 = int(x[2])
    if m + m_1 >= 60:
        m = m + m_1 - 60
        h += 1
    else:
        m += m_1

    if h + h_1 >= 24:
        h = h + h_1 - 24
    else:
        h += h_1

    print(f"{str(h).zfill(2)}:{str(m).zfill(2)}")

