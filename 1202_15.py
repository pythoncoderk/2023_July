import itertools

l = list(map(int, input().split()))
price_list = l[1:]
print(price_list)
counts = l[0]
print(counts)
patterns = list(itertools.permutations(price_list))
print(patterns)



