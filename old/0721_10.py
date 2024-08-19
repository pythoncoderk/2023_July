x, y, n = map(int, input().split())

a1 = n // 3
b1 = n % 3

a_answer = a1 * y + b1 * x


a2_answer = x * n


print(a_answer if a_answer < a2_answer else a2_answer)