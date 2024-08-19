a, b, c, d = map(int, input().split())

count = 0
tf = 0
kf = 0

if c == 0 or d == 0:
    print("miss")
    exit()

for i in range(1, b + 1):
    t = i
    k = b - i
    if k <= 0:
        break
    tr = t * c
    kr = k * d
    if tr + kr == a:
        count += 1
        if tr >= 1:
            tf = tr // c
        if kr >= 1:
            kf = kr // d

if count == 1 and tf + kf == b and (tf >= 1 and kf >= 1):
    print(tf, kf)
else:
    print("miss")