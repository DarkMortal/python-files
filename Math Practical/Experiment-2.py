f = lambda x:(x+1/x)

a = 1.2
b = 1.6
n = 4

if __name__ == "__main__":
    d = (b-a)/n
    x = (f(a)+f(b))/2
    for i in range(1,n):
        x += f(a+i*d)
    x *= d
    print(round(x,3))

#Output: 0.848