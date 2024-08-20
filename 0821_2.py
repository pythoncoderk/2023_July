n = int(input())

f = 1
for i in range(2, n + 1):
    f *= i

f = list(str(f))

count = 0
while True:
    x = f.pop()
    if x != "0":
        print(count)
        break
    else:
        count += 1