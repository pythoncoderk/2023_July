class Test:
    __pi = 3

    def ok(self, r):
        return r * 2 * Test.__pi



# print(Test.__pi)
print(Test().ok(5))