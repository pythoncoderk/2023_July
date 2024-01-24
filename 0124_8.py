s = list(map(str, input().split("+")))
# print(s)
total_l = 0

for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] == "/":
            total_l += 1
        elif s[i][j] == "<":
            total_l += 10

print(total_l)