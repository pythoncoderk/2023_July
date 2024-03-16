l = list(map(int, input().split()))

if l[0] > l[2]:
    print("Aoki")
elif l[0] < l[2]:
    print("Takahashi")
else:
    if l[1] > l[3]:
        print("Aoki")
    elif l[1] < l[3]:
        print("Takahashi")
    else:
        print("Takahashi")