l = [int(input()) for i in range(4)]
x = 0
for i in range(4):
    if i + 1 not in l:
        x = i + 1
print(x)