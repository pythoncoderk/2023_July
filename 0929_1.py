for i in range(9):
    for j in range(9):
        if j == 8:
            print(f'{str((i + 1) * (j + 1)).rjust(2, " ")}')
            if i == 8:
                pass
            else:
                print("==========================================")
        else:
            print(f'{str((i + 1) * (j + 1)).rjust(2, " ")} | ', end="")
