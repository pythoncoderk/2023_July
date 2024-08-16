n, q = map(int, input().split())

l = [i for i in range(1, n + 1)]

for i in range(q):
    x = input().split()
    if x[0] == "reverse":
        l = l[::-1]
    elif x[0] == "resize":
        l = l[:int(x[1])]
    else:
        l[int(x[1]) - 1], l[int(x[2]) - 1] = l[int(x[2]) - 1], l[int(x[1]) - 1]

for i in l:
    print(i)
