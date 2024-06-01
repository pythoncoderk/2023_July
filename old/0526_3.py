s = list(input())
# print(s)

b_count = s.count(")")

l = []
i = 0
while s.count("*") != b_count:
    if s[i] == "(":
        l.append(i+1)
        i += 1
    elif s[i] == ")":
        x = l.pop()
        y = i + 1
        s[i] = "*"
        i += 1
        print(x, y)