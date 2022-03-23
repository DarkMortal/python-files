import math as m

def myfunc(n):
  return int(m.log2(n))

if __name__=="__main__":
    x = list(map(myfunc,[2,4,8,16,32]))
    print(type(x[0]))