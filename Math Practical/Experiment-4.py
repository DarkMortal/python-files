from math import sqrt

if __name__ == "__main__":
    x = [1,2,3,4]
    y = [4,7,3,3]
    m = sum([x[i]*y[i] for i in range(len(x))])/sum(y)
    v = sum([(x[i]**2)*y[i] for i in range(len(x))])/sum(y)-(m**2)
    print("Mean =",round(m,3))
    print("Variance =",round(v,3))
    print("Standard Deviation =",round(sqrt(v),3))

'''Output

Mean = 2.294
Variance = 1.031
Standard Deviation = 1.015

'''