n = int(input())
l = list(map(int, input().split()))
print(n)
print(l)

count = True
for i in range(n):
    if l[i] % 2 != 0:
        count = False



