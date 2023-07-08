# def test():
#     print("Hello")
#
# test()

def deco(func):
    def wrapper(*args, **kwargs):
        print("--start--")
        func(*args, **kwargs)
        print("--end--")
    return wrapper

@deco
def test():
    print("Hello World!")
test()