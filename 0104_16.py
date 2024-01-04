n = int(input())
l = list(map(int, input().split()))
m = int(input())

# print(n)
# print(l)
# print(m)
final_count = 0
for i in l:
    if i == m:
        final_count += 1
print(final_count)