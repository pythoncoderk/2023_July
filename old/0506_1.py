n = [5, 8, 9]
k = 20

x = 1

bin_num = bin(x)
bin_num = list(bin_num)
print(bin_num)

l = []
for i in range(len(bin_num)):
    if i != 0 and i != 1:
        l.append(int(bin_num[i]))

l.sort()

count = 0

total = 0
for i in range(len(l)):
    if l[i] == 1:
        total += n[i]
    if total == k:
        count += 1
