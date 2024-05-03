d, n, l = map(int, input().split())
l2 = [int(input()) for i in range(n)]

# print(d, n, l)
# print(l2)

now1 = 0
count = 0
def dai1(now, pulus, max_count):
    count = 0
    while now != pulus:
        now += 1
        count += 1
        if now >= max_count:
            now = 0
    return count

def dai2(now, pulus, max_count):
    count = 0
    while now != pulus:
        now -= 1
        count += 1
        if now < 0:
            now = max_count-1
    return count


for i in range(n):
    one = dai1(now1, l2[i], d)
    two = dai2(now1, l2[i], d)
    if one > two:
        now1 = l2[i]
        count += two
    else:
        now1 = l2[i]
        count += one

# print(count)

if count < l:
    print("Yes")
else:
    print("No")







