class test(object):
    def test_funcx(self, x, y):
        """
        >>> t = test()
        >>> t.test_funcx(2, 2)
        9
        """
        result = x * y
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
