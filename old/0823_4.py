n = int(input())

count_ans = 0
for i in range(2, n + 1):
    prime_num = True
    count = 0
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
    if count >= 2:
        prime_num = False
    if prime_num:
        count_ans += 1
print(count_ans)