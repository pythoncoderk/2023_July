n = int(input())
l = list(map(int, input().split()))
l.sort()

# print(n)
# print(l)

l_c = [l.count(l[i]) for i in range(n)]
# print(l_c)

max_l = max(l_c)
# print(max_l)
l_final = [l[i] for i in range(n) if l_c[i] == max_l]
# print(l_final)

l_final = set(l_final)
l_final = list(l_final)
l_final.sort()

print(*l_final)