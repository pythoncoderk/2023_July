n = int(input())
a, b = map(int, input().split())

p = 1
k = 1
now_name = "p"
count = 0
while k <= n:
    if now_name == "p":
        k += p * a
        now_name = "k"
        count += 1
    else:
        p += k % b
        now_name = "p"

print(count)