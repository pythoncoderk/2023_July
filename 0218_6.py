n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

# print(n)
# print(l1)
# print(l2)

total = 0
for i in range(n):
    total += l1[i] * l2[i]

if total == 0:
    print("Yes")
else:
    print("No")