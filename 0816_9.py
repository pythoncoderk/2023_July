l = []

while True:
    x = list(map(int, input().split()))
    x = x[::-1]
    l = x + l
    if len(x) == 1:
        break


for i in range(len(l)):
    if l[i] == 1:
        print(i + 1)
        break

print(sum(l))