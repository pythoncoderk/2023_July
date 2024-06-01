n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, m)
# print(l)

l_en = [l[i][0] for i in range(n)]
l_en.sort()
l_en_f = [l_en[i] for i in range(m)]
# print(l_en_f)

l_jp = [l[i][1] for i in range(n)]
l_jp.sort()
l_jp_f = [l_jp[i] for i in range(m)]
# print(l_jp_f)

l_math = [l[i][2] for i in range(n)]
l_math.sort()
l_math_f = [l_math[i] for i in range(m)]
# print(l_math_f)

ls = [l_en_f, l_jp_f, l_math_f]
# print(ls)

for i in range(n):
    f_count = 0
    for j in range(3):
        if l[i][j] in ls[j]:
            f_count += 1
    print(f_count)