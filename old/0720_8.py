import itertools

n, k = map(int, input().split())
s = list(input())

l = []
x = list(itertools.permutations(s, n))

l2 = []
for i in range(len(x)):
    l2.append("".join(x[i]))

l_s = set(l2)
l_s = list(l_s)

count = 0

for i in range(len(l_s)):
    if "yyy" not in l_s[i]:
        count += 1
print(count)


