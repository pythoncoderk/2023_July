n = input()
m = int(input())
l = [input() for i in range(m)]

# print(n)
# print(m)
# print(l)

count = 0
for i in range(m):
    if n not in l[i]:
        count += 1
        print(l[i])

if count == 0:
    print("none")