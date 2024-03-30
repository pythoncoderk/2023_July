n = int(input())
l = list(map(str, input().split()))
l2 = ["and", "not", "that", "the", "you"]

# print(n)
# print(l)

for i in range(n):
    if l[i] in l2:
        print("Yes")
        exit()
print("No")