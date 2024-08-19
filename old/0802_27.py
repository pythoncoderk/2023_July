n = int(input())
l = input().split()
m = int(input())
l2 = [int(i) for i in input().split()]

for i in range(m):
    print(l[l2[i] - 1])