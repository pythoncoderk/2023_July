n, x = map(int, input().split())
l = [int(input()) for i in range(n)]

total = ""
while x != 0:
    total += str(x % 2)
    x //= 2


for i in range(n):
    print(total[int(l[i])-1])
