s = input()
t = input()

final = ""

for i in range(len(t)):
    x = t[i]
    if x.islower():
        x = ord(x) - 97
        final += s[x]
    else:
        x = ord(x) - 65
        final += s[x]

print(final)