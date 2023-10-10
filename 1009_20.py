n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

for i in range(m):
    print(l[l2[i]-1])