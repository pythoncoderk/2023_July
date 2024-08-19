n = int(input())

count = {}

for _ in range(n):
    s = input()
    if s not in count:
        count[s] = 1
    else:
        count[s] += 1

for word, times in sorted(count.items()):
    print(word, times)