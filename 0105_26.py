n = int(input())
l = [input() for i in range(n)]
total = 0
for i in l:
    if i == "correct":
        total += 2
    elif i == "incorrect":
        total -= 1
print(total)