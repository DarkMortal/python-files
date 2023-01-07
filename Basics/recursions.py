def Pow(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return x*Pow(x,n-1)

def factorial(x):
    if x<0:
        raise ValueError("Expects value greater than or equal to 0")
    elif x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

if __name__=="__main__":
    try:
        print(Pow(4,3))
        print(factorial(5))
    except ValueError as err:
        print(err)