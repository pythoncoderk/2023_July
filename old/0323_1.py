t = int(input())
l = [input() for i in range(t)]

# print(t)
# print(l)

times = 0
count = 0
for i in range(t):
    if l[i] == "melon" and times <= 0:
        count += 1
        times = 10
    else:
        times -= 1
print(count)