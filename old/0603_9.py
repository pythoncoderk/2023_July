s = list(input())

print("Won" if s.count(s[0]) == len(s) else "Lost")