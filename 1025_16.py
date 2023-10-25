n = int(input())
if n >= 70:
    print("very noisy")
elif n >= 50 and n < 70:
    print("noisy")
elif n >= 30 and n < 50:
    print("normal")
else:
    print("quiet")