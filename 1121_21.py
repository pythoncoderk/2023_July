n = int(input())
m = list(input())
for i in range(n):
    if i == n-1:
        print(m.pop())
    else:
        print(m.pop(), end="")