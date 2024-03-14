l = list(map(int, input().split()))

l_s = set(l)
l_s = list(l_s)
# print(l_s)
# print(l)

if len(l_s) == 2:
    if (l.count(l_s[0]) == 3 and l.count(l_s[1]) == 2) or (l.count(l_s[0]) == 2 and l.count(l_s[1]) == 3):
        print("Yes")
    else:
        print("No")
else:
    print("No")