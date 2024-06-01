s = list(input())
# print(s)

l = [int(s[i]) for i in range(len(s)) if s[i] != "-"]
# print(l)

count = 0
for i in range(len(l)):
    if l[i] == 0:
        count += 12
    else:
        count += l[i]+2
print(count * 2)