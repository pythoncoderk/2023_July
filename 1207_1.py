n = int(input())
l = [[int(i) for i in input().split()] for _ in range(n)]
k = int(input())

xn, yn = l[-1]
answer = 0

for xi, yi in l:
    if abs(xi - xn) + abs(yi - yn) <= k:
        print(abs(xi - xn) + abs(yi - yn))
        answer += 1
print(answer)