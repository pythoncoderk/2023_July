n = int(input())
s = input()

# print(n)
# print(s)

l = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

l1 = l[n:] + l[:n]

# print(l1)

l2 = l[-n:] + l[:-n]

# print(l2)

for i in range(len(s)):
    if i % 2 == 0:
        x = ord(s[i])-65
        print(l2[x], end="")
    else:
        x = ord(s[i])-65
        print(l1[x], end="")