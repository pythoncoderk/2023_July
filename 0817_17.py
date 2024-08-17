n = int(input())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

for i in range(n):
    print(l[i] - l2[i])