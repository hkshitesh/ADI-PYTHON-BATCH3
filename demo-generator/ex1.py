def f1():
    res=10
    return res

#print(f1())


def f2():
    yield 10
    yield 20
    yield 30

res= f2()
print(next(res))
print(next(res))