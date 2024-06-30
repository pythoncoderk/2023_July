n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

for i in range(len(l)):
    for j in range(len(l)):
        if i != j:
            for k in range(len(l)):
                if k != j and k != i:
                    if l[i] + l[j] + l[k] == 1000:
                        print("Yes")
                        exit()

print("No")
