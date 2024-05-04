s = list(input())
t = list(input())

print(s)
print(t)

l2 = [[i+1, t[i]] for i in range(len(t))]
print(l2)

l3 = l2[::]


def chk(arr, ss):
    while True:
        x = len(arr) // 2
        l4 = arr[x:]
        l5 = arr[:x]
        if len(l4) > len(l5):
            max_l = len(l4)
        else:
            max_l = len(l5)
        for i in range(max_l):
            if ss == l4[i][1]:
                arr = l4
                break
            arr = l5

print(chk(l3, "c"))