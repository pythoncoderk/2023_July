n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

max_l = l[0]

for i in range(len(l)):
    if l[i] > max_l:
        print(i+1)
        exit()

print(-1)
