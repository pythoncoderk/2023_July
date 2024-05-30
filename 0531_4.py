s = list(input())

s2 = []
x_s = ""
while len(s) >= 1:
    x = s.pop(0)
    if x_s != "" and not x.isdecimal():
        s2.append(x_s)
        x_s = ""
    if not x.isdecimal():
        s2.append(x)
    else:
        x_s += x

if x_s != "":
    s2.append(x_s)

# print(s2)

final = ""
for i in range(len(s2)):
    if s2[i].isdecimal():
        x = int(s2[i]) + 1
        x = str(x)
        final += x
    else:
        x = ord(s2[i])
        x += 1
        if x >= 91:
            x -= 26
        final += chr(x)

print(final)