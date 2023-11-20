n = int(input())
l = list(map(str, input().split()))
if l.count("G") == l.count("P"):
    print("Draw")
elif l.count("G") < l.count("P"):
    print("G")
else:
    print("P")