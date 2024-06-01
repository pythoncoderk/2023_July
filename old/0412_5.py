n = int(input())
l = [input() for i in range(2)]

# print(n)
# print(l)

for i in range(n):
    if l[0] == l[1]:
        print("Yes")
        exit()
    else:
        l[1] = l[1][-1] + l[1][:-1]
print("No")

