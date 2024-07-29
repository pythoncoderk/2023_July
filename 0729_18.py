n = input()
m = n[::-1]

# print(n)
# print(m)

answer = ""
for i in range(len(m)):
    if i != len(m) - 1 and (i + 1) % 3 == 0:
        answer += m[i] + ","
    else:
        answer += m[i]

print(answer[::-1])