s = list(input())
a, b = map(int, input().split())

s[a - 1], s[b - 1] = s[b - 1], s[a - 1]


answer = ""
for i in range(len(s)):
    answer += s[i]

print(answer)