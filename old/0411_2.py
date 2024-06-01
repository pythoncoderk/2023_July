d, n, l = map(int, input().split())
l2 = [int(input()) for i in range(n)]

print(d, n, l)
print(l2)


def select(x, y, z):
    now = y
    next_c = z
    count_a = 0
    while now != next_c:
        count_a += 1
        now += 1
    max_x = x + y
    next_c2 = z
    count_b = 0
    while max_x != next_c2:
        count_b += 1
        max_x -= 1

    if count_a > count_b:
        return count_b
    else:
        return count_a

total = 0
count = 0
d = d - 1
point = 0
for i in range(n):
    xxx = select(d, point, l2[i])
    point = l2[i]
    total += xxx
    count += 1
print(total)
