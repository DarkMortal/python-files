from math import sqrt

def cors(x,y):
    n = len(x)
    a = sum(x)
    b = sum(y)
    a2 = sum([i*i for i in x])
    b2 = sum([i*i for i in y])
    ab = sum([x[i]*y[i] for i in range(n)])
    l = sqrt(n*a2-a*a)
    t = sqrt(n*b2-b*b)
    return (n*ab-a*b)/(l*t)

if __name__ == "__main__":
    x = [2,3,5,6,7]
    y = [5,7,11,13,15]
    print(round(cors(x,y),3))

#Output: 1.0