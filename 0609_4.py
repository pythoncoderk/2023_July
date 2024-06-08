s = list(input())

l_count = [s.count(s[i]) for i in range(len(s))]

# print(l_count)

print("Yes" if l_count.count(2) == 4 else "No")