for i in range(1, 10):
    for j in range(1, 10):
        if j == 9 and i != 9:
            print(f"{i*j}")
            print("==========================================")
        else:
            if i == 9 and j == 9:
                print(f"{i * j}")
            else:
                print(f"{i*j} | ", end="")