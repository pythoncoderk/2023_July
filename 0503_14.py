n = int(input())
a = input()
b = input()

# print(n)
# print(a)
# print(b)

for i in range(len(a)):
    x = a[-1] + a[:-1]
    a = x
    if x == b:
        print("Yes")
        exit()

print("No")