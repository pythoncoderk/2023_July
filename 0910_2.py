s = ["a", "b", "c"]
print(s)
print(s[0])
s[0] = "XXX"
print(s)

s[1:2] = ["B", "C"]
print(s)

s[1:2] = []
print(s)

s[:] = []
print(s)

a = [1,2,3]
b =[4,5,6]
print(a + b)


print(a.extend(b))