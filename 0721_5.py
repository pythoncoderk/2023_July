s = input()

l = [s.count(s[i]) for i in range(len(s))]

# print(l)

count = False
for _ in range(len(l)):
    if l[_] == 1:
        count = True
        print(s[_])
        exit()

if not count:
    print(-1)