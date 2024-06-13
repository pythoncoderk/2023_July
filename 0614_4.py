l = [list(input()) for i in range(3)]

# print(l)

answer = ""
x = 0
for i in range(3):
    answer += l[i][x]
    x += 1

print(answer)