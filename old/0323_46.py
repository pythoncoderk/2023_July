count = 0
l = [int(input()) for i in range(7)]

for i in range(7):
    if l[i] <= 30:
        count += 1

print(count)