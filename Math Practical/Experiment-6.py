from math import sqrt

def regression(x,y):
    n = len(x)
    a = sum(x)
    b = sum(y)
    a2 = sum([i*i for i in x])
    b2 = sum([i*i for i in y])
    ab = sum([x[i]*y[i] for i in range(n)])
    mx = a/n
    my = b/n
    vx = a2/n-mx**2
    vy = b2/n-my**2
    sdx = sqrt(vx)
    sdy = sqrt(vy)
    cov = ab/n-mx*my
    bxy = cov/(sdy**2)
    byx = cov/(sdx**2)
    return (mx,my,bxy,byx)

if __name__ == "__main__":
    x = [2,3,5,6,7]
    y = [5,7,11,13,15]
    (a,b,c,d) = (round(n,1) for n in regression(x,y))
    print("Y -",b,"=",d,"*(X -",a,")")
    print("X -",a,"=",c,"*(Y -",b,")")

'''Output
Y - 10.2 = 2.0 *(X - 4.6 )
X - 4.6 = 0.5 *(Y - 10.2 )
'''