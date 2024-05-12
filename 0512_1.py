n, x = map(int, input().split())
l = list(map(int, input().split()))
l_index = [i for i in range(1, len(l)+1)]

# print(n, x)
# print(l)
# print(l_index)

l2 = [l, l_index]
# print(l2)

def s1(arr, x):
    l_main = arr[0]
    l_index_chk = arr[1]
    half = len(l_main) // 2

    l_a = l_main[:half]
    l_b = l_main[half:]

    l_a_index = l_index_chk[:half]
    l_b_index = l_index_chk[half:]

    in_chk = False
    for i in range(len(l_a)):
        if x == l_a[i]:
            in_chk = True
            break
    if in_chk:
        return [l_a, l_a_index]
    else:
        return [l_b, l_b_index]


while len(l2[0]) != 1:
    l2 = s1(l2, x)

print(l2[1][0])