s, t = map(str, input().split())

if len(t) == 1:
    print("No")
    exit()

l = []
for i in range(len(t)):
    for j in range(len(s)):
        if t[i] == s[j]:
            l.append(j)
            break
# print(l)

l_x = l[::]
l_x.sort()

if l != l_x:
    print("No")
    exit()

if len(t) != len(l):
    print("No")
    exit()

l2 = []
for i in range(len(l) - 1):
    l2.append(l[i + 1] - l[i])

# print(l2)

x = len(l2)
y = l2.count(l2[0])

print("Yes" if x == y else "No")