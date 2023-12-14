# coding: utf-8
l = [1,2,3,4,5]

x = l[0]
y = l[-1]

x, y = y, x

l[0] = x
l[-1] = y

print(l)