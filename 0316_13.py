s = input()

l = []
for i in range(1, len(s)+1):
    l2 = []
    for j in range(1, len(s)+1):
        if 1 <= i < j <= len(s):
            l2.append(i)
            l2.append(j)
        if l2:
            l.append(l2)
            l2 = []
        else:
            l2 = []
# print(s[l[0][0]-1])
# print(l)
s2 = list(s[::])
s = list(s)
final = []
for i in range(len(l)):
    s[l[i][0]-1] = s2[l[i][1]-1]
    s[l[i][1]-1] = s2[l[i][0]-1]
    final.append(s)
    s = s2[::]
l_final = []
for i in range(len(final)):
    chk = ""
    for j in range(len(final[i])):
        chk += final[i][j]
    l_final.append(chk)

l_final = set(l_final)
l_final = list(l_final)
print(len(l_final))