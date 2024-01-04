n = int(input())
l = []
for i in range(2, n+1):
    if n % i == 0:
        l.append(i)

if len(l) >= 1:
    print("NO")
else:
    print("YES")