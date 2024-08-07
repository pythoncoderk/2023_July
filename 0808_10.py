s = input().split("/")
x, y = s[-1].split(":")

final = s[:-1]
final.append(x)
final.append(y)

for i in final:
    print(i)