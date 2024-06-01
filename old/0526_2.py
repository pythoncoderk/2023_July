s = list(input())

while s.count("*") != len(s):
    x = 0
    for i in range(len(s)):
        if s[i] == ")":
            x = i + 1
            s[i] = "*"
            break
    s_index = 9999
    for i in range(x-1, -1, -1):
        if s[i] == "(":
            s_index = i
            s[i] = "*"
            break
    print(s_index + 1, x)
