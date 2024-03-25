s = input()
n = int(input())

for i in range(len(s)):
    if i != n - 1:
        print(s[i], end="")