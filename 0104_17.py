n = int(input())
l = list(map(int, input().split()))
m = int(input())
x = 0
for i in range(n):
    if l[i] == m:
        print(i+1)
        x += 1
        break
if x == 0:
    print(0)


