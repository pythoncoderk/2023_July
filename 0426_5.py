l = list(input())

l = [1 if l[i] == "/" else l[i] for i in range(len(l))]
l = [10 if l[i] == "<" else l[i] for i in range(len(l))]
l = [l[i] for i in range(len(l)) if l[i] != "+"]

print(sum(l))