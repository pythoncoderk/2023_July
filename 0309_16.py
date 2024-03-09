n = int(input())
s = input()

a = False
b = False
c = False
x = 0
for i in range(n):
    if s[i] == "A":
        a = True
    elif s[i] == "B":
        b = True
    elif s[i] == "C":
        c = True

    if a == True and b == True and c == True:
        print(i+1)
        exit()
    else:
        x = i
print(x)

