s = input()
s_l = [s[i] for i in range(len(s))]


s1 = s_l[::]

l = []
text = ""
while s1:
    if text == "":
        if s1[0].isdecimal():
            text += s1.pop(0)
        else:
            l.append(s1.pop(0))
    else:
        if s1[0].isdecimal():
            text += s1.pop(0)
        else:
            l.append(text)
            text = ""
l.append(text)
# print(l)

for i in range(len(l)):
    if l[i].isalpha():
        l[i] = ord(l[i])
        l[i] += 1
        if l[i] >= 91:
            l[i] -= 26
        l[i] = chr(l[i])

for i in range(len(l)):
    if l[i].isdecimal():
        l[i] = int(l[i])
        l[i] += 1

for i in l:
    print(i, end="")