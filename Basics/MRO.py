# MRO stands for Method Resolution Order
# It says that whenever there is multiple inheritance of 
# 2 or more parent classes by one base class, 
# unlike c++,in case of an overloading,
# the methods and constructors are called in order of left to right 

class A:
    #Python variant of function object of c++
    def __call__(self, x):
        return "Value passed from classA = "+str(x)
    def __init__(self):
        print("Constructor of class A is called")

class B:
    def __call__(self, x):
        return "Value passed from classB = "+str(x)
    def __init__(self):
        print("Constructor of class B is called")

class C(A,B):
    pass

if __name__=="__main__":
    a=C()
    print(a("Hello"))
