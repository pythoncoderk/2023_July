n, x = map(int, input().split())
l = list(map(int, input().split()))

# print(n, x)
# print(l)

count = 0
for i in range(len(l)):
    if l[i] == x:
        count += 1

if count >= 1:
    print("Yes")
else:
    print("No")