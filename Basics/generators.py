# Generators in python are functions that return iterators

def myGenerator(n, someFunc = lambda x:x):
    x = 0
    while x <= n:
        x += 1
        yield someFunc(x)

# driver code
if __name__ == "__main__":
    arr1 = myGenerator(5)
    arr2 = myGenerator(5, lambda x:x*x)

    for i in arr1:
        print(i, end = " ")
    print()
    
    for i in arr2:
        print(i, end = " ")
    print()