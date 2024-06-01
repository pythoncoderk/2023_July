n = int(input())
g = input()
l = [input() for i in range(n)]

# print(n)
# print(g)
# print(l)
count = 0
for i in range(n):
    if g in l[i]:
        print(l[i])
        count += 1

if count == 0:
    print("None")