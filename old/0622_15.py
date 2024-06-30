s = input()
n = int(input())

l = []
for i in range(len(s)):
    for j in range(len(s)):
        l.append(s[i] + s[j])

print(l[n - 1])