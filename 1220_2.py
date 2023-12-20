n = int(input())
l = list(map(int, input().split()))
l2 = [i+1 for i in range(n) if l[i] % 2 == 1]
print(l2[-1])