def division(a,b):
    print(a/b)

def division_decorator(func):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return func(x,y)
    return inner


division = division_decorator(division)
division(5,10)