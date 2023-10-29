n = int(input())
l = [int(input()) for i in range(n)]
l = list(set(l))
print(len(l))