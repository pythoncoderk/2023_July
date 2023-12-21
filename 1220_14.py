n, k = map(int, input().split())
l = [int(input()) for i in range(n * k)]
# print(n, k)
# print(l)
l2 = [(l[i] + l[i+1] + l[i+2])/k for i in range((n * k)-2)]
# print(l2)
l_min = min(l2)
print(l.index(l_min)+1)
