s = input()
n = int(input())

total = 0
for i in range(len(s)):
    if s[i] == "R":
        total += 1

if total >= n:
    print("Yes")
else:
    print("No")