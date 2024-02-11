l = list(map(int, input().split()))
s = input()

# print(l)
# print(s)

for i in range(len(s)):
    x = ord(s[i]) - 97
    if l[x] >= 1:
        print(s[i], end="")
        l[x] -= 1


