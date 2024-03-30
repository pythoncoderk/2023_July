n = int(input())
l = [i for i in range(0, 101, 5)]
# print(l)

l2 = [abs(l[i] - n) for i in range(len(l))]
# print(l2)

x = l2.index(min(l2))
print(l[x])