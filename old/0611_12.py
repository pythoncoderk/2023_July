n = input()
answer = ""
for i in range(len(n)):
    if n[i] == "1":
        answer += "9"
    else:
        answer += "1"
print(answer)