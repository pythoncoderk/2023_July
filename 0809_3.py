s = input()
farst = True
total = 0
ans = ""
while s:
    if s[0] == "+":
        if farst:
            total = int(ans)
            ans = ""
            farst = False
        else:
            total += int(ans)
            ans = ""
            s = s[1:]
    elif s[0] == "-":
        if farst:
            total = int(ans)
            ans = ""
            farst = False
        else:
            total -= int(ans)
            ans = ""
            s = s[1:]
    else:
        ans += s[0]
        s = s[1:]

print(total + int(ans))