n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

l_set = set(l)
l_set = list(l_set)

# print(l_set)

l2 = [l.count(l_set[i]) for i in range(len(l_set))]
# print(l2)

max_l = max(l2)
for i in range(len(l_set)):
    if l2[i] == max_l:
        print(l_set[i])