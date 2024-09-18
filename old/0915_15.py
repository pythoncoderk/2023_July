n = input()

x = len(n) - 1

answer = 0
for i in n:
    answer += (2 ** x) * int(i)
    x -= 1

print(answer)