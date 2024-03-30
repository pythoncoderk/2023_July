s = input()

changes = ""

for i in range(len(s)):
    if s[i].isdecimal():
        changes += s[i]
    else:
        x = ord(s[i]) + 1
        if x >= 91:
            x -= 26
        changes += chr(x)

chk3 = ""
k = 0
changes2 = ""
while changes != "":
    chk2 = ""
    if changes[0].isdecimal():
        chk3 += changes[0]
        changes = changes[1:]
    elif chk3 != "":
        chk3 = int(chk3)+1
        chk3 = str(chk3)
        changes2 += chk3
        chk3 = ""
    else:
        chk2 += changes[0]
        changes = changes[1:]
        changes2 += chk2

if chk3 != "":
    chk3 = int(chk3)+1
    chk3 = str(chk3)
print(changes2 + chk3)