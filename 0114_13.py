n = int(input())
num = bin(n)
x = -1
counts = 0
for i in range(len(num)):
    if num[x] == "0":
        counts += 1
        x -= 1
    else:
        break
print(counts)