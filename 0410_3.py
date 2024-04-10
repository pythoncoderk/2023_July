n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

for i in range(n-1):
    if l[i][-1] != l[i+1][0]:
        print(l[i][-1], l[i+1][0])
        exit()
print("Yes")