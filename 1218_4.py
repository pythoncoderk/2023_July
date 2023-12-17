n = int(input())
l = list(map(int, input().split()))

l2 = [i for i in l if i % 2 == 1 or i == 0]
# print(l)
# print(l2)
counts = 0
while len(l2) == 0:
    l = [i//2 for i in l]
    l2 = [i for i in l if i % 2 == 1]
    counts += 1
print(counts)