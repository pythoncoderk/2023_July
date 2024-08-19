n = 3
k = 20

l = [5, 8, 9]
count = 0
x = 0
while True:
    b = bin(x)[2:]
    b_l = list(b.zfill(3))
    x += 1
    count_l = b_l.count("1")
    total = 0
    for i in range(len(l)):
        if b_l[i] =


    if count_l == n:
        break
