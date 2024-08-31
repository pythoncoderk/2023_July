import itertools

n = int(input())
l = list(map(int, input().split()))
for i in range(3, n + 1):
    for pair in itertools.combinations(l, i):
        print(pair)