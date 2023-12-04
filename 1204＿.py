num = input()
n = int(input())
l = [input() for i in range(n)]
print(num)
print(n)
print(l)
for i in l:
    if num == i:
        print("first")
    elif int(i)+1 == int(num) or int(i)-1 == int(num):
        print("adjacent")
    elif i[-4] == num[-4]:
        print("second")
    elif i[-3] == num[-3]:
        print("third")
    else:
        print("blank")