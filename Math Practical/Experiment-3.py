from math import sqrt

f = lambda x: sqrt(3*x*x+5*x+1.02)

a = 1
b = 2
n = 50

if __name__ == "__main__":
    d = (b-a)/n
    x = f(a) + f(b)
    for i in range(1,n):
        x += (2*f(a+i*d) if i%2 == 0 else 4*f(a+i*d))
    x *= d/3
    print(round(x,3))

#Output: 3.905