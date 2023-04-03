#Changing the behaviour of the function without changing the function itself.
def smart_pow(func):

    def inner(*args, **kwargs):
        if isinstance(args[1], float) or args[1] < 0.0:
            return func(args[0]**args[1], 1)
        else:
            return func(*args, **kwargs)

    return inner


#smart_pow is a decorator for the function pow
@smart_pow
def pow(x, y):
    if y == 0:
        return 1
    return x * pow(x, y - 1)


#Changing the behaviour of the function without changing the function itself.
def smart_fact(func):

    def inner(*args, **kwargs):
        if args[0] < 0:
            raise ArithmeticError("Argument can't be less than 0")
        if isinstance(args[0], float):
            from math import gamma
            return gamma(args[0]+1.0)
        else:
            return func(*args, **kwargs)

    return inner


#smart_fact is a decorator for the function fact
@smart_fact
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

# driver code
if __name__ == "__main__":
    try:
        print(pow(2, 3))
        print(pow(2, 3.5))

        print(fact(5))
        print(fact(5.5))
        
        print(fact(-2.0))
    except Exception as exc:
        print(str(exc))