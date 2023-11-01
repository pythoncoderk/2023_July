l = list(map(int, input().split()))
x = 0
for i in l:
    if i <= 2:
        x += 1
print(x)