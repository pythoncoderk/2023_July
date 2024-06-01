l = list(input().split())
s = input()
l2 = [int(l[i]) for i in range(len(l)) if l[i] != " "]

# print(l2)
# # print(s)
# print(len(l2))

for i in range(len(s)):
    x = ord(s[i])-97
    if len(l2) >= x:
        if l2[x] >= 1:
            print(s[i], end="")
            l2[x] -= 1

