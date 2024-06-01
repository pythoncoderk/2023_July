x = input()
count = 0
for i in range(365):
    if x in str(i):
        count += 1
print(count)