b = input()
n = int(input())
l = [input() for i in range(n)]

# print(b)
# print(n)
# print(l)

for i in range(n):
    if b == l[i]:
        print("f")
    elif int(b) == int(l[i])+1 or int(b) == int(l[i])-1:
        print("a")
    elif b[-4:] == l[i][-4:]:
        print("s")
    elif b[-3:] == l[i][-3:]:
        print("t")
    else:
        print("b")