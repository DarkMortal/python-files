def regression(x,y):
    n = len(x)
    a = sum(x)
    b = sum(y)
    a2 = sum([i*i for i in x])
    b2 = sum([i*i for i in y])
    ab = sum([x[i]*y[i] for i in range(n)])
    p = 1
    q = 1

if __name__ == "__main__":
    #something
    x = [2,3,5,6,7]
    y = [5,7,11,13,15]
    (a,b) = regression(x,y)