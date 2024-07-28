h, w = map(int, input().split())
s1, s2 = map(int, input().split())
l = [list(input()) for i in range(h)]
x = list(input())

h -= 1
w -= 1

s1 -= 1
s2 -= 1

# print(h, w)
# print(s1, s2)
# print(l)
# print(x)

# print(l[s1][s2])

for i in x:
    if i == "U":
        if s1 - 1 >= 0:
            if l[s1 - 1][s2] == ".":
                s1 -= 1
    elif i == "D":
        if s1 + 1 <= h:
            if l[s1 + 1][s2] == ".":
                s1 += 1
    elif i == "R":
        if s2 + 1 <= w:
            if l[s1][s2 + 1] == ".":
                s2 += 1
    elif i == "L":
        if s2 - 1 >= 0:
            if l[s1][s2 - 1] == ".":
                s2 -= 1

print(s1 + 1, s2 + 1)