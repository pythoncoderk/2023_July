n = int(input())
l = [input() for i in range(n)]
l_set = set(l)
l_set_2 = list(l_set)
# print(l_set_2)

l_count = [l.count(i) for i in l_set_2]
# print(l_count)

d = dict(zip(l_count, l_set_2))
# print(d)

d2 = sorted(d.items(), reverse=True)
print(d2[0][1])