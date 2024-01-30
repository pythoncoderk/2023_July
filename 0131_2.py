t = int(input())
l = [input() for i in range(t)]
# print(l)
count = 0
wait = 0
melon_eat = True

for i in range(t):
    if l[i] == "apple" and melon_eat:
        melon_eat = False
        count += 1
    else:
        if not melon_eat:
            wait += 1
            if wait >= 10:
                wait = 0
                melon_eat = True

print(count)