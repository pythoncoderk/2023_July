n = int(input())
l = list(map(int, input().split()))

avg = sum(l) // n
for i in range(n):
    print(abs(avg - l[i]))