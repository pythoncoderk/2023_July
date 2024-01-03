n, k, m = map(int, input().split())
print(n, k, m)
l_k = [input() for i in range(k)]
l_m = [input() for i in range(m)]

print(l_k)
print(l_m)
l2 = []
output = 0
def first(word):
    global output
    output = 1
    if word in l_k:
        return True

def second(word):
    global j
    if word in l_k and l_m[j][0] == l_m[j-1][-1] and l_m[-1] != "z":
        return True
    else:
        return False

for j in range(m):
    if output == 0:
        word = l_m[j]
        if first(word):
            output = 1
        else:
            if j % n == 0:
                l2.append(n)
            else:
                l2.append(j % n)
            output = 0
    else:
        word = l_m[j]
        if second(word):
            output = 1
        else:
            if j % n == 0:
                l2.append(n)
            else:
                l2.append(j % n)
            output = 0
print(l2)