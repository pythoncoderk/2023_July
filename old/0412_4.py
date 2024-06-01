n, m, k = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(n, m, k)
# print(l)

count = 0
get = 0
for i in range(n):
    if count >= k:
        print(get)
        exit()
    else:
        if i+1 not in l:
            get += 1
            count = 0
        else:
            count += 1
print(get)
