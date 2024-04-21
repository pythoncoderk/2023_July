s = input()

d = {"A": 4, "E": 3, "G": 6, "I": 1, "O": 0, "S": 5, "Z": 2}
for i in s:
    if i in d:
        print(d[i], end="")
    else:
        print(i, end="")