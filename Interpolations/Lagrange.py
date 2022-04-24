def Lagrange(x,y,a):
    Y=0
    for i in range(len(x)):
        num=1
        den=1
        for j in range(len(x)):
            if x[i] != x[j]:
                num *= (a-x[j])
                den *= (x[i]-x[j])
        num *= y[i]
        Y += (num/den)
    return Y

if __name__ == "__main__":
    x=list(range(6))
    y=[5.2,8.0,10.4,12.4,14.0,15.2]
    print(round(Lagrange(x,y,0.5),3))