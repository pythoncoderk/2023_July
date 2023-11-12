import sys

n = int(input())
paiza = [1, 1]
monster = [1, 1]
battel = 0
i = 0
j = 1
i2 = 0
j2 = 1
count = 2
if n == 1:
    print(1)
    sys.exit()

while n > sum(paiza):
    if battel == 0:
        monster.append(paiza[i] + paiza[j])
        battel = 1
        i += 1
        j += 1
        count += 1
    else:
        paiza.append((monster[i2]) + (monster[j2]*2))
        battel = 0
        i2 += 1
        j2 += 1


print(count)