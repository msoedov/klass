

def Klass(**fields):
    """[summary]

    Returns:
        [type] -- [description]

    >>> Klass(a=1, b=2).a
    1
    """

    return type('DataClass', (object,), fields)


def main():
    pass


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
