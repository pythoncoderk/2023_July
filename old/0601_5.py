n = int(input())
l = [0, 0, 0]

while n != 0:
    if n - 26 > 26:
        if l[0] < 26:
            l[0] += 1
            n -= 1
        else:
            if l[1] < 26:
                l[1] += 1
                n -= 1
            else:
                if l[2] < 26:
                    l[2] += 1
                    n -= 1

