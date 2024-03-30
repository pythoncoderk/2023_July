class cal(object):
    def test_chk(self, x, y):
        """
        >>> c = cal()
        >>> c.test_chk(1, 9)
        10

        """

        result = x + y
        return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()