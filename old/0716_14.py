a, b, c, d, e, f, x = map(int, input().split())

print(a, b, c, d, e, f, x)


answer_1 = x // (a + c)
answer_2 = x % (a + c)

answer_t = ((answer_1 * a) + answer_2) * b

print(answer_t)


answer_3 = x // (d + f)
answer_4 = x % (d + f)

answer_a = ((answer_3 * d) + answer_4) * e

print(answer_t)


