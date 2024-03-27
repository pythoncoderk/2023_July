import itertools

l = list(map(str, input().split()))

x = list(itertools.permutations(l))
# print(x)

final = []
for i in range(len(x)):
    a = x[i][0] + x[i][1]
    b = x[i][2] + x[i][3]
    final.append(int(a) + int(b))

print(max(final))