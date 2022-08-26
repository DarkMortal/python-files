import math

'''PS : Find the number of ways that a given integer, X, can be expressed as the sum of the Nth powers of unique, natural numbers.'''

def recurse(X,N,arr):
    if X == 0:
        return 1
    if len(arr) == 0 or X<0:
        return 0
    return recurse(X-(arr[-1]**N),N,arr[0:-1])+recurse(X,N,arr[0:-1])

def powerSum(X, N):
    arr = list(range(1,int(math.pow(X,1/N))+1))
    return recurse(X,N,arr)

print(powerSum(10,2))