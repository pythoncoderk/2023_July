s = list(input())

print(s)

final = ""
chk = False
while not chk:
    if len(s) <= 1:
        chk = True
    x = s.pop(0)
    if x.isdecimal() == False:
        x = ord(x)
        x += 1
        if x >= 91:
            x -= 26
            final += chr(x)
        else:
            final += chr(x)
    else:
        while not chk:
            if len(s) == 1:
                chk = True
            if s[0].isdecimal():
                y = s.pop(0)
                x += y
            else:
                x = int(x)
                x += 1
                x = str(x)
                final += x

print(final)