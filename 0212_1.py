N, A, B = map(int, input().split())
l_A = [list(input()) for i in range(A)]

# print(N, A, B)
# print(l_A)
x = 0
for i in range(N):
    if len(l_A[1]) <= A and x != len(l_A[1]):
        if l_A[0][i] == l_A[1][x]:
            x += 1
if x == 0:
    x_total = A
else:
    x_total = len(l_A[1]) - x

y = 0
for i in range(N):
    if len(l_A[2]) <= B and y != len(l_A[2]):
        if l_A[0][i] == l_A[2][y]:
            y += 1
if y == 0:
    y_total = B
else:
    y_total = len(l_A[2]) - y

print(f"{x_total} {y_total}")


