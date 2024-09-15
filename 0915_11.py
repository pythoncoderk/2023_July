n = int(input())

answer = ""
while n > 0:
    x = n % 2
    y = n // 2
    answer += str(x)
    n = y

answer = answer[::-1]
print(answer.zfill(10))