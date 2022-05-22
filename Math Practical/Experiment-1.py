from math import pi 

abs = lambda x: (x if x>0 else x*(-1))

if __name__ == "__main__":
    n = int(input())
    approx = 0
    k = 1
    for i in range(1,n+1):
        if i%2 == 0:
            approx -= 1/k
        else:
            approx += 1/k
        k += 2
    approx *= 4
    abs_error = abs(pi-approx)
    rel_error = abs_error/pi
    print('Exact =',pi)
    print('Approx =',approx)
    print('Absolute Error =',abs_error)
    print('Relative Error =',rel_error)
    print('Percentage Error =',rel_error*100)