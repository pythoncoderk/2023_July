class A(Exception):
    pass

def func1():
    try:
        func2()
    except A:
        print("B")

def func2():
    print("C")
    raise A
    print("D")

func1()