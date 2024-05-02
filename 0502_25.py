x = input()
count = 0
for i in range(0, 366):
    n = str(i)

    if x in n:
        count += 1

print(count)
