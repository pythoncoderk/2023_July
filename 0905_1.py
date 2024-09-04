n = int(input())
x, y = map(int, input().split())

# print(n)
# print(x, y)

p = 1
k = 1

entry = True
count = 0
while True:
    if entry:
        k += p * x
        count += 1
        entry = False
        if n < k:
            print(count)
            exit()
    else:
        p += k % y
        entry = True