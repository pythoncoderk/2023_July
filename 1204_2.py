l = list(map(str, input().split()))
# print(l)
while l:
    print(f"{l[0]} {l.count(l[0])}")
    # x = l[0]
    l = [i for i in l if i != l[0]]