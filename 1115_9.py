n = input()
m = int(input())
l = [input() for i in range(m)]

for i in range(m):
    if l[i] == n:
        print("first")
    elif int(l[i]) == int(n) - 1 or int(l[i]) == int(n) + 1:
        print("adjacent")
    elif l[i][-4:] == n[-4:]:
        print("second")
    elif l[i][-3:] == n[-3:]:
        print("third")
    else:
        print("blank")