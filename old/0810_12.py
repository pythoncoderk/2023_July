s = list(input())

x = ""
total = 0
cal = ""
while s:
    if s[0].isdecimal():
        x += s.pop(0)
    else:
        if cal == "":
            if x == "":
                cal = s.pop(0)
            else:
                total += int(x)
                x = ""
        elif cal == "+":
            total += int(x)
            x = ""
            cal = ""
        else:
            total -= int(x)
            x = ""
            cal = ""
print(total + int(x) if cal == "+" else total - int(x))






