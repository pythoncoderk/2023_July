l = list(map(int, input().split()))

l2 = [i for i in range(l[0], l[1]+1)]
l3 = [i for i in range(l[2], l[3]+1)]

# print(l2)
# print(l3)

x = set(l2) & set(l3)
if len(x) - 1 >= 0:
    print(len(x) - 1)
else:
    print(0)