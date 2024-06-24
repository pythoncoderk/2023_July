s = input()
l = []

a = ord(s[0])
b = ord(s[1])
c = ord(s[2])

l.append(a)
l.append(b)
l.append(c)

l.sort()

answer = ""
for i in range(3):
    answer += chr(l[i])

print("Yes" if answer == "abc" else "No")