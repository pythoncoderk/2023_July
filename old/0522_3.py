n, q = map(int, input().split())

l = [int(input()) for i in range(n)]
l2 = [int(input()) for i in range(q)]


def binary_search(l, x):
    while True:
        search_point = len(l) // 2
        binary_l1 = l[:search_point]
        binary_l2 = l[search_point:]

        chk = False
        if not binary_l1:
            y = binary_l2
            chk = True
        elif not binary_l2:
            y = binary_l1
            chk = True
        if x in binary_l1:
            l = binary_l1
        else:
            l = binary_l2
        if chk:
            return y


for i in range(q):
    output = binary_search(l, l2[i])
    print("YES" if output[0] == l2[i] else "NO")