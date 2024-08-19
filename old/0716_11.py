s = list(map(int, input()))

print(s)

answer = ""

for i in range(len(s)):
    x = s[i] - 1
    if x <= 0:
        answer += str(0)
    else:
        answer += str(1)

print(answer)