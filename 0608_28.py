n = int(input()) - 1

l = [
    ["#", "#", "#"],
    ["#", ".", "#"],
    ["#", "#", "#"]
    ]

l2 = []
for i in range(3 ** n):
    for j in range(3 ** n):
        l2.append(l)

print(l2)