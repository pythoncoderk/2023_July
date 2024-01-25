s = input()
n = int(input())
l = list(map(str, input().split()))

counts = 0
for i in range(n):
    if l[i] == s:
        counts += 1

if counts >= 1:
    print("Yes")
else:
    print("No")