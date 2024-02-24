s = input()

l = []
for i in range(len(s)):
    l.append(s.count(s[i]))
# print(l)
for i in range(len(l)):
    if l[i] == 1:
        print(i+1)