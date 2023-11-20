n = int(input())
l = [int(input()) for i in range(7)]
if n <= sum(l):
    print(n)
else:
    print(sum(l))