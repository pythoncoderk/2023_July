x = int(input())

l = [500, 100, 50, 10, 5, 1]
l2 = l[::]
x2 = x

l_f = []
count = 0
i = 0
k = 0
while l2:
        while x > 0:
            x -= l2[i]
            count += 1
        while x != 0:
            if abs(x) >= l[k]:
                x += l[k]
                count += 1
            else:
                k += 1
        l_f.append(count)
        count = 0
        l2.pop(0)
        x = x2
        k = 0
print(l_f)