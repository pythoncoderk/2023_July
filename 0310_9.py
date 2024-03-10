n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)
count = 0
for i in range(n):
    if l[i] % 2 != 0:
        print(count)
        exit()

while True:
    for i in range(n):
        l[i] = int(l[i] / 2)
    count += 1
    for i in range(n):
        if l[i] % 2 != 0:
            print(count)
            exit()
