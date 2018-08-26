### Klass

Fast, extensible and lightweight dataclasess for Python 2 /3

```python
>>> class A(Klass(a=1, b=2)):
        pass
>>> A.a
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
```
