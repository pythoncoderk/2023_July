n = int(input())
s = input()

ff = 0

if n == 1:
    print("Yes")
    exit()

for i in range(n-1):
    if s[i] == s[i+1]:
        ff += 1

if ff >= 1:
    print("No")
else:
    print("Yes")