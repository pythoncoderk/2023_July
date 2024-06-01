n, k = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, k)
# print(l)

print("YES" if k in l else "NO")
