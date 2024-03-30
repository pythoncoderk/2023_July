l = list(map(str, input().split()))

x_l = 0
for i in range(5):
    if l[i] == "x":
        x_l = i

i_l = 0
for i in range(5):
    if l[i] == "=":
        i_l = i

if i_l < x_l:
    if l[1] == "+":
        print(int(l[0]) + int(l[2]))
    else:
        print(int(l[0]) - int(l[2]))
else:
    x = ""
    for i in range(5):
        if l[i] != "+" and l[i] != "-" and l[i] != "x":
            x = l[i]
            break
    y = int(l[-1])
    if l[1] == "+":
        x = int(x) * -1
    x += y

print(y)
