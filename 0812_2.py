s = input()
t = input()

final = ""
for i in range(len(s)):
    x = s[i]
    y = t[i]
    z = str(int(x) + int(y))
    ans = z[-1]
    final += ans

print(final)