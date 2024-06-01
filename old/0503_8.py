n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

for i in range(n-1):
    x = l[i][-1]
    y = l[i+1][0]
    if x != y:
        print(x, y)
        exit()

print("Yes")