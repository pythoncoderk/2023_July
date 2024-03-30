l = [input() for i in range(3)]

max_l = 0
for i in l:
    if max_l < len(i):
        max_l = len(i)

print(max_l)