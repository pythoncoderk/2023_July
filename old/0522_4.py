n, q = map(int, input().split())
s = {int(input()) for i in range(n)}

for i in range(q):
    x = int(input())
    print("YES" if x in s else "NO")