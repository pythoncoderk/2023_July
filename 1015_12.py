n = int(input())
l = list(map(int, input().split()))

l1 = [i for i in l if i % 2 == 0]
l2 = [i for i in l if i % 2 != 0]
print(len(l1), end=" ")
print(len(l2))
