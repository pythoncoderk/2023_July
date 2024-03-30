n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

if n == 1:
    print(0)
    exit()

one = l[0]
two = l[1:]
max_two = max(two)

if one > max_two:
    print(0)
else:
    print(max_two - one + 1)