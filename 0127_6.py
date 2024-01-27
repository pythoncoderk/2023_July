h, w = map(int, input().split())
r, c = map(int, input().split())
l = [list(input()) for i in range(h)]

r -= 1
c -= 1

# print(h, w)
# print(r, c)
# print(l)
x = 0
y = 0
r1 = r
c1 = c
l[r1][c1] = "#"
#case 1
count_case1 = 0
l2 = l[::]
for i in range(h-1):
    if r1 + i+1 > h-1:
        break
    else:
        if l2[r1+i+1][c1] == "#":
            count_case1 += 1
            break
        # else:
        #     l2[r1+i+1][c1] = "#"
l2 = l[::]
if count_case1 >= 1:
    for i in range(h-1):
        if r1 + i+1 > h-1:
            break
        else:
            if l2[r1+i+1][c1] == "#":
                break
            else:
                l2[r1+i+1][c1] = "#"

#case 2
r1 = r
c1 = c
count_case2 = 0
l2 = l[::]
for i in range(h-1):
    if r1 - i-1 < 0:
        break
    else:
        if l2[r1-i-1][c1] == "#":
            count_case2 += 1
            break
        # else:
        #     l2[r1-i-1][c1] = "#"
l2 = l[::]
if count_case2 >= 1:
    for i in range(h-1):
        if r1 - i-1 < 0:
            break
        else:
            if l2[r1-i-1][c1] == "#":
                break
            else:
                l2[r1-i-1][c1] = "#"

#case 3
r1 = r
c1 = c
count_case3 = 0
l2 = l[::]
for i in range(h-1):
    if c1 - i-1 < 0:
        break
    else:
        if l2[r1][c1-i-1] == "#":
            count_case3 += 1
            break
        # else:
        #     l2[r1][c1-i-1] = "#"
l2 = l[::]
if count_case3 >= 1:
    for i in range(h-1):
        if c1 - i-1 < 0:
            break
        else:
            if l2[r1][c1-i-1] == "#":
                break
            else:
                l2[r1][c1-i-1] = "#"

#case 4
r1 = r
c1 = c
count_case4 = 0
l2 = l[::]
for i in range(h-1):
    if c1 + i+1 > w-1:
        break
    else:
        if l2[r1][c1+i+1] == "#":
            count_case4 += 1
            break
        # else:
        #     l2[r1][c1+i+1] = "#"
l2 = l[::]
if count_case4 >= 1:
    for i in range(h-1):
        if c1 + i+1 > w-1:
            break
        else:
            if l2[r1][c1+i+1] == "#":
                break
            else:
                l2[r1][c1+i+1] = "#"

#case 5
r1 = r
c1 = c
count_case5 = 0
l2 = l[::]
for i in range(h-1):
    if r1-i-1 < 0 or c1-i-1 < 0:
        break
    else:
        if l2[r1-i-1][c1-i-1] == "#":
            count_case5 += 1
            break
        # else:
        #     l2[r1-i-1][c1-i-1] = "#"
l2 = l[::]
if count_case5 >= 1:
    for i in range(h-1):
        if r1-i-1 < 0 or c1-i-1 < 0:
            break
        else:
            if l2[r1-i-1][c1-i-1] == "#":
                break
            else:
                l2[r1-i-1][c1-i-1] = "#"

#case 6
r1 = r
c1 = c
count_case6 = 0
l2 = l[::]
for i in range(h-1):
    if r1-i-1 < 0 or c1+i+1 > w-1:
        break
    else:
        if l2[r1-i-1][c1+i+1] == "#":
            count_case6 += 1
            break
        # else:
        #     l2[r1-i-1][c1+i+1] = "#"
l2 = l[::]
if count_case6 >= 1:
    for i in range(h-1):
        if r1-i-1 < 0 or c1+i+1 > w-1:
            break
        else:
            if l2[r1-i-1][c1+i+1] == "#":
                break
            else:
                l2[r1-i-1][c1+i+1] = "#"

#case 7
r1 = r
c1 = c
count_case7 = 0
l2 = l[::]
for i in range(h-1):
    if r1+i+1 > h-1 or c1+i+1 > w-1:
        break
    else:
        if l2[r1+i+1][c1+i+1] == "#":
            count_case7 += 1
            break
        # else:
        #     l2[r1+i+1][c1+i+1] = "#"
l2 = l[::]
if count_case7 >= 1:
    for i in range(h-1):
        if r1+i+1 > h-1 or c1+i+1 > w-1:
            break
        else:
            if l2[r1+i+1][c1+i+1] == "#":
                break
            else:
                l2[r1+i+1][c1+i+1] = "#"

#case 8
r1 = r
c1 = c
count_case8 = 0
l2 = l[::]
for i in range(h-1):
    if r1+i+1 > h-1 or c1-i-1 < 0:
        break
    else:
        if l2[r1+i+1][c1-i-1] == "#":
            count_case8 += 1
            break
        # else:
        #     l2[r1+i+1][c1-i-1] = "#"
l2 = l[::]
if count_case8 >= 1:
    for i in range(h-1):
        if r1+i+1 > h-1 or c1-i-1 < 0:
            break
        else:
            if l2[r1+i+1][c1-i-1] == "#":
                break
            else:
                l2[r1+i+1][c1-i-1] = "#"

for i in range(h):
    for j in range(w):
        print(l[i][j], end="")
    print()