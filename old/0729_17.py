n = input()
answer = ""
for i in range(len(n)):
    if (i + 1) % 3 == 0 and i != len(n) - 1:
        answer += n[i] + ","
    else:
        answer += n[i]

print(answer)