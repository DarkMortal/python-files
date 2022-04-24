import math as m

def isSame(arr):
    if len(arr) == 0:
        return False
    v=arr[0]
    for i in arr:
        if i == v:
            continue
        else:
            return False
    return True

def diffTable(y):
    diff = []
    diffs = [y]

    #Creating the difference table
    while(len(diff)!=1 or not isSame(diff)):
        if len(diffs) == 1:
            for i in range(len(y)-1):
                diff.append(y[i+1]-y[i])
            diffs.append(diff)
        else:
            temp = []
            for i in range(len(diff)-1):
                temp.append(diff[i+1]-diff[i])
            diffs.append(temp)
            diff = temp

    return diffs

def Forward(x,y,a):
    X=a
    Y=y[0]

    def factors(a,n):
        if n == 0:
            return a
        return (a-n)*factors(a,n-1)
    
    diffs = diffTable(y)

    #Forward Interpolation begins
    h=x[1]-x[0] #Assuming the intervals to be equal
    p=(X-x[0])/h
    dels=[e[0] for e in diffs]

    for i in range(len(dels)-1):
        num=dels[i+1]*factors(p,i)
        den=m.factorial(i+1)
        Y+=(num/den)
    return Y

def Backward(x,y,a):
    X=a
    Y=0

    def factors(a,n):
        if n == 0:
            return a
        return (a+n)*factors(a,n-1)

    diffs = diffTable(y)

    #Backward Interpolation begins
    h=x[1]-x[0] #Assuming the intervals to be equal
    p=(X-x[-1])/h
    dels=[e[-1] for e in diffs]
    Y=dels[0]

    for i in range(len(dels)-1):
        num=dels[i+1]*factors(p,i)
        den=m.factorial(i+1)
        Y+=(num/den)
    return Y

if __name__ == "__main__":
    x=list(range(6))
    y=[5.2,8.0,10.4,12.4,14.0,15.2]
    print(round(Forward(x,y,0.5),3))
    print(round(Backward(x,y,0.5),3))
