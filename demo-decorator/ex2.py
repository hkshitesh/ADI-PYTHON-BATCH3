def upper_decorator(func):
    def inner():
        result = func()
        return result.upper()
    return inner


@upper_decorator
def say_hello():
    return "hello world"

res= say_hello()
print(res)

@upper_decorator
def say_bye():
    return "bye world"

res2= say_bye()
print(res2)
