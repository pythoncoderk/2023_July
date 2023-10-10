for i in range(9):
    for j in range(9):
        if j+1 == 9:
            print(str((i + 1) * (j + 1)).rjust(2, " "))
            if i+1 == 9:
                pass
            else:
                print("=" * 42)
        else:
            print(str((i + 1) * (j + 1)).rjust(2, " "), end=" | ")