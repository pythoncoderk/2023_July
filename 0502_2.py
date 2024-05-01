n, a, b = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, a, b)
# print(l)

count = 0
money = 0
for i in range(n):
    if i == n-1:
        money += count * l[i]
    elif l[i] <= a:
        count += 1
        money -= l[i]
    elif l[i] >= b:
        money += count * l[i]
        count = 0


print(money)
