import itertools

s = list(input())
s2 = s
s3 = ""
s_f = []
while s:
    s3 += s.pop(0)
    x = list(itertools.permutations(s3))
    s_f.append(x)

s = list(s3)
while s:
    s4 = ""
    s4 += s.pop(0)
    x = list(itertools.permutations(s4))
    s_f.append(x)



print(s_f)
s_f2 = []
for i in range(len(s_f)):
    for j in range(len(s_f[i])):
        s_f2.append(s_f[i][j])

s_f2 = set(s_f2)
s_f2 = list(s_f2)
print(s_f2)

s_f3 = []
for i in range(len(s_f2)):
    s5 = ""
    for j in range(len(s_f2[i])):
        s5 += s_f2[i][j]
    s_f3.append(s5)

print(s_f3)
s_f4 = []
for i in range(len(s_f3)):
    if s_f3[i] in s3:
        s_f4.append(s_f3[i])
print(len(s_f4))



