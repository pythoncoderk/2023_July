n = int(input())
l = [input() for i in range(n)]

melon_c = 0
eats = 0
for i in range(n):
    if eats <= 0 and l[i] == "melon":
        melon_c += 1
        eats = 10
    else:
        eats -= 1
print(melon_c)
