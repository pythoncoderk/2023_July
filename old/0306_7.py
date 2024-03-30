s = input()
l = [s.count(s[i]) for i in range(len(s))]
# print(l)

print(l.index(1)+1)