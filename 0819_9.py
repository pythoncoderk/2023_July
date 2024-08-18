N = int(input())

digit_sum = 0
while N > 0:
    digit_sum += N % 10
    N //= 10

print(digit_sum)