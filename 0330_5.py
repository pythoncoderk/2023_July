n = int(input())
s = input()

l = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z"
]
# print(l)

l1 = l[n:]
l2 = l[:n]
l_o = l1 + l2
#
# print(l_o)

l3 = l[-n:]
l4 = l[:-n]
l_t = l3 + l4

# print(l_t)

total = ""
for i in range(len(s)):
    if i % 2 == 0:
        x = ord(s[i]) - 65
        total += l_t[x]
    else:
        x = ord(s[i]) - 65
        total += l_o[x]
print(total)