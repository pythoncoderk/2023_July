l = [int(input()) for i in range(5)]
k = int(input())

# print(l)
# print(k)

count = True

for i in range(len(l)):
    for j in range(len(l)):
        if i != j:
            if abs(l[i] - l[j]) > k:
                count = False

print("Yay!" if count else ":(")