with open("test.txt", "r") as f:
    print(f.tell())
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
    f.seek(5)
    print(f.read(1))