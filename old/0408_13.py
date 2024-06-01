n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

min_l = min(l)
for i in range(n):
    if l[i] == min_l:
        print(i+1)
        exit()