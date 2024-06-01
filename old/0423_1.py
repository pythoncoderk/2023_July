n, s, p = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, s, p)
# print(l)

l2 = [l[i][0] if s - p <= l[i][1] <= s + p else 0 for i in range(n)]
# print(l2)

max_l = max(l2)
if max_l != 0:
    for i in range(n):
        if l2[i] == max_l:
            print(i+1)
            break
else:
    print("not found")