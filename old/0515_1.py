import bisect

n, k = map(int, input().split())
l = list(map(int, input().split()))

print(n, k)
print(l)

l2 = [i for i in range(1, k+1)]

print(l2)

len_l = k // 2

print(len_l)

x = bisect.bisect_left(l2, len_l)

a = l2[:x]
b = l2[x:]
z = a[-1]

print(a)
print(b)
print(z)




