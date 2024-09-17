b = int(input())
n = int(input())

for i in range(n):
    num = input()
    if b == int(num):
        print("first")
    elif int(num) + 1 == b or int(num) - 1 == b:
        print("adjacent")
    elif num[-4:] == str(b)[-4:]:
        print("second")
    elif num[-3:] == str(b)[-3:]:
        print("third")
    else:
        print("blank")
