n = input()
ans = 0
for i in range(len(n)):
    x = 2 ** (len(n) - 1 - i)
    if n[i] == "1":
        ans += x
print(ans)