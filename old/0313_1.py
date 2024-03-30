n = int(input())
s = input()

r = 0
x = 0

for i in range(n):
    if s[i] == "o":
        r += 1
    elif s[i] == "x":
        x += 1

if r >= 1 and x == 0:
    print("Yes")
else:
    print("No")