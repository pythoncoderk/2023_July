s = input()
answer = ""
for i in range(len(s)):
    if s[i] == "A":
        answer += "4"
    elif s[i] == "E":
        answer += "3"
    elif s[i] == "G":
        answer += "6"
    elif s[i] == "I":
        answer += "1"
    elif s[i] == "O":
        answer += "0"
    elif s[i] == "S":
        answer += "5"
    elif s[i] == "Z":
        answer += "2"
    else:
        answer += s[i]
print(answer)
