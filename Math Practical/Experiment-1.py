from math import pi 

abs = lambda x: (x if x>=0 else x*(-1))

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
    print('Exact =',round(pi,6))
    print('Approx =',round(approx,6))
    print('Absolute Error =',round(abs_error,6))
    print('Relative Error =',round(rel_error,6))
    print('Percentage Error =',round(rel_error*100,6))

'''Output

69
Exact = 3.141593
Approx = 3.156085
Absolute Error = 0.014492
Relative Error = 0.004613
Percentage Error = 0.461294

'''