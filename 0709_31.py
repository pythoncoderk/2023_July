n, k = map(int, input().split())
s = input()

answer = ""
for i in range(n):
    if i == k - 1:
        answer += s[i].lower()
    else:
        answer += s[i]

print(answer)