# from icecream import ic
# ic.disable()
a = int(input())

l = []
for i in range(1, a + 1):
    for j in range(1, a + 1):
        if i + j == a:
            l.append(i * j)
# ic(l)
print(max(l))