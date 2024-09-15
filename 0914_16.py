n, t = map(str, input().split())
n = int(n)

s = list(input())

# print(t)
# print(s)

if n == 0:
    ans = "".join(s)

for j in range(n):
    ans = ""
    for i in range(len(s)):
        if s[i] == " ":
            ans += " "
        else:
            ans += chr(t.index(s[i]) + 97)
    s = ans


print(ans)