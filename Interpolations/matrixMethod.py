from numpy import *

def solve(x,y,a):
    arr1 = []
    arr2 = [[e] for e in y]

    degree = len(x)-1

    for i in x:
        temp = []
        for j in range(len(x)):
            temp.append(i**(degree-j))
        arr1.append(temp)

    res=0
    matrix1 = array(arr1)
    matrix2 = array(arr2)
    matrix1 = linalg.inv(matrix1)
    resultant = matrix1.dot(matrix2)
    result = [float(e[0]) for e in resultant]

    for i in range(len(result)):
        res += (result[i]*(a**(degree-i)))
    return res

if __name__ == "__main__":
    x=list(range(6))
    y=[5.2,8.0,10.4,12.4,14.0,15.2]
    print(round(solve(x,y,0.5),3))