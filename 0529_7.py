n = int(input())

def binary(x):
    x1 = x // 2
    x2 = 0 if x % 2 == 0 else 1
    return x1, x2


total = ""
while n >= 1:
    answer1, answer2 = binary(n)
    total = str(answer2) + total
    n = answer1

print(total.zfill(10))
