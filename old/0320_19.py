x = input()

y = x[-1]
# print(y)

index_l = x.index(".")
# print(index_l)

xx = x[:index_l]
# print(xx)

if 0 <= int(y) <= 2:
    yy = "-"
elif 7 <= int(y) <= 9:
    yy = "+"
else:
    yy = ""

print(f"{xx}{yy}")