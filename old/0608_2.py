n, m = map(int, input().split())

n_l = [i for i in range(2, (n * 2) + 1, 2)]
m_l = [i for i in range(1, (m * 2) + 1, 2) if i % 2 != 0]
n_m_l = n_l + m_l

# print(n_l)
# print(m_l)
# print(n_m_l)

count = 0
for i in range(len(n_m_l)):
    for j in range(i, len(n_m_l)):
        if i != j:
            x = n_m_l[i] + n_m_l[j]
            if x % 2 == 0:
                count += 1

print(count)
