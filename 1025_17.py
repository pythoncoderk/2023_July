s = input()
l = ["Monday", "Tuesday", "Wednesday", "Thursday"]
if s in l:
    print(f"Still {l[l.index(s)]}")
else:
    print("TGIF")