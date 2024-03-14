s = list(input())
# print(s)

s_f = []
while s:
    s_f.append(s.pop(1))
    s_f.append(s.pop(0))

for i in s_f:
    print(i, end="")