n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

count = 0
eat = 10
while l:
    x = l.pop(0)
    if eat >= 10 and x == "melon":
        eat = 0
        count += 1
    else:
        eat += 1

print(count)
