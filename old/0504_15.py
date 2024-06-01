import random

l = [1, 2, 5, 8, 10]

key = random.randint(1, 10)
print(str(key) + "が含まれているかチェック")

for i in range(len(l)):
    if l[i] == key:
        print(i)
        exit()
print("None")
