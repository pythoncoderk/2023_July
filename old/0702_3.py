n = int(input())

answer = ""
while n != 0:
    if n % 2 == 0:
        answer += "0"
        n //= 2
    else:
        answer += "1"
        n //= 2

answer = answer[::-1]
print(answer.zfill(10))