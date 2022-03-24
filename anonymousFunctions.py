#Anonymous Functions are python variant of lambda function of c++
import math as m

f=lambda x:3*x*x
g=lambda x:m.sqrt(x)

if __name__=="__main__":
    fog=lambda x:int(round(f(g(x)),0))
    print(fog(2))  #should print 6
    arr=range(2,20)
    arr=list(map(fog,arr))
    print(arr)