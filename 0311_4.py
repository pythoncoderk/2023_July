n = int(input())
s = input()

t = 0
a = 0

t2 = 0
a2 = 0

for i in range(n):
    if s[i] == "T":
        t += 1
    else:
        a += 1

if t > a:
    print("T")
elif t < a:
    print("A")
else:
    for i in range(n):
        if s[i] == "T":
            t2 += 1
            if t2 == t:
                print("T")
                exit()
        else:
            a2 += 1
            if a2 == a:
                print("A")
                exit()
