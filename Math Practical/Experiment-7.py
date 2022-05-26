def fit(x,y):
    n = len(x)
    a = sum(x)
    b = sum(y)
    a2 = sum([i*i for i in x])
    ab = sum([x[i]*y[i] for i in range(n)])
    p = round((n*ab-a*b)/(n*a2-a*a),3)
    q = round((b-a*p)/n,3)
    return (p,q)

if __name__ == "__main__":
    x = [1,2,3,4,6]
    y = [7,9,11,13,17]
    (a,b) = fit(x,y)
    print("Y = ",a,"X +",b)

#Output: Y =  2.0 X + 5.0