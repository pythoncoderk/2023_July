n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

l2 = [l[i] for i in range(n) if l[i] % 2 == 0]
print(*l2)