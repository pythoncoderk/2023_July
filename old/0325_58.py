s = input()

x = s[1:]

if x.count(x[0]) == len(x):
    print("Yes")
else:
    print("No")