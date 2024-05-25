n = int(input())
m = int(input())

l1 = [i for i in range(1, n+1) if n % i == 0]
l2 = [i for i in range(1, m+1) if m % i == 0]

# print(l1)
# print(l2)

l1_set = set(l1)
l2_set = set(l2)

# print(l1_set)
# print(l2_set)

x = l1_set & l2_set

if len(x) == 1:
    print("yes")
else:
    print("no")