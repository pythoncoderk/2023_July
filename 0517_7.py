n = input()
s = n[::-1]

count = 0
count_i = 1
for i in range(len(n)):
    x = int(s[i])
    count += x * count_i
    count_i *= 2

print(count)