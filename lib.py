def Klass(**fields):
    """[summary]

    Returns:
        [type] -- [description]

    >>> Klass(a=1, b=2).a
    1
    >>> cl = Klass(a=1, b=2)
    >>> cl(a=3).a
    3
    >>> cl(g=3)
    Traceback (most recent call last):
     ...
    NameError: Unkown argument g=3
    >>> cl(a=3) == cl(a=3)
    True
    >>> cl(a=2) == cl(a=3)
    False
    >>> cl() in {cl(): 1}
    True
    >>> cl(a=4) in {cl(a=5): 1}
    False
    >>> cl()
    &data._({'a': 1, 'b': 2, '__data__': ['a', 'b']})
    """
    fields["__data__"] = list(fields.keys())

    class _(type("DataClass", (object,), fields)):
        def __init__(self, **class_kwargs):
            for k, val in class_kwargs.items():
                if k not in fields:
                    raise NameError("Unkown argument {}={}".format(k, val))
                setattr(self, k, val)

        def __str__(self):
            return "&data.{}({})".format(self.__class__.__name__, fields)

        __repr__ = __str__

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

        def __hash__(self):
            return hash(tuple(fields[k] for k in fields["__data__"]))

    return _


def main():
    pass


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod()
