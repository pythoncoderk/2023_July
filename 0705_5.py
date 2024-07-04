l = list(map(int, input().split()))

# print(l)

for i in range(1, 4):
    if l[0] == l[1]:
        print(-1)
        exit()
    elif i not in l:
        print(i)
        exit()

print(-1)