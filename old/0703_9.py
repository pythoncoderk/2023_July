l = list(map(int, input().split()))



l.sort(reverse=True)

# print(l)

print(l[0] * 10 + l[2] + l[1] * 10 + l[3])
