# We are going to use tabular version of dynamic programming

'''PS : Given an amount and the denominations of coins available, 
determine how many ways change can be made for amount. There is a limitless supply of each coin type.'''

def getWays(n, c):
    perms = [1]+[0]*n
    for coin in c:
        for i in range(coin,n+1):
            perms[i] += perms[i-coin]
    return perms[n]

# Driver Code
if __name__ == "__main__":
    print(getWays(4,[1,2,3]))