def pow(x,y):
    if y == 0:
        return 1
    return x*pow(x,y-1)

#Changing the behaviour of the function without changing the function itself.
def smart_pow(func):
    def inner(a,b):
        if isinstance(b,float) :
            a = a**b
        return func(a,1)
    return inner

print(smart_pow(pow)(2,4.5))
#smart_pow is a decorator for the function pow