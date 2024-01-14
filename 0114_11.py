for i in range(1, 101):
    if i % 15 == 0:
        print(f"{i}:HogeFuga")
    elif i % 3 == 0:
        print(f"{i}:Hoge")
    elif i % 5 == 0:
        print(f"{i}:Fuga")
    else:
        print(f"{i}:")