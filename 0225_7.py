l = [8, 10, 2, 5, 1, 4, 6, 3, 7, 9]

for i in range(len(l)):
    for j in range(-1, i + len(l) * -1, -1):
        if l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]

print(l)

"""
出力内容
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""