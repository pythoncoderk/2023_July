s = int(input())
s2 = str(s)
n = int(input())
l = [int(input()) for i in range(n)]

for i in l:
    if i == s:
        print("first")
    elif i - 1 == s or i + 1 == s:
        print("adjacent")
    elif s2[-4:] == str(i)[-4:]:
        print("second")
    elif s2[-3:] == str(i)[-3:]:
        print("third")
    else:
        print("blank")