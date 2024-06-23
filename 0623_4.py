
count1 = 1
count2 = 1
count3 = 0

for i in range(36):
    if i == 0 or i == 1:
        print(1)

    else:
        count3 = count1 + count2
        print(count3)
        count1 = count2
        count2 = count3

