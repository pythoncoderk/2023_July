a, b = map(int, input().split())

diff = abs(a - b) / 2
x_diff = int(diff)
if diff != x_diff:
    print("IMPOSSIBLE")
    exit()

a_answer = diff + a if a < b else a - diff
b_answer = b - diff if a < b else diff + b

print(int(a_answer))