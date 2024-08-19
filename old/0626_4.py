n = input()
m = int(input())
l = [input() for i in range(m)]

x = int(n)
x_1 = x - 1
x_2 = x + 1


# print(n)
# print(m)
# print(l)

for i in range(m):
    if n == l[i]:
        print("first")
    elif int(l[i]) == x_1 or int(l[i]) == x_2:
        print("adjacent")
    elif n[-4:] == l[i][-4:]:
        print("second")
    elif n[-3:] == l[i][-3:]:
        print("third")
    else:
        print("blank")
