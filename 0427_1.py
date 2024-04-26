s = list(input())

l = [1 if s[i] == "/" else s[i] for i in range(len(s))]

# print(l)

l2 = [10 if l[i] == "<" else l[i] for i in range(len(s))]

# print(l2)

l3 = [0 if l2[i] == "+" else l2[i] for i in range(len(s))]

print(sum(l3))