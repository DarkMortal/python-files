# PS: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

parenthesis = []

def binomialCoeff(n, k):
    res = 1
    # Since C(n, k) = C(n, n-k)
    if (k > n - k):
        k = n - k
    # Calculate value of [n*(n-1)*---
    # *(n-k+1)] / [k*(k-1)*---*1]
    for i in range(k):
        res *= (n - i)
        res /= (i + 1)
    return int(res)

# TODO: Total number of balanced strings can be found by catalan numbers
def catalan(n):
    # Calculate value of 2nCn
    c = binomialCoeff(2 * n, n)
    # return 2nCn/(n+1)
    return int(c / (n + 1))

# TODO: Check if the given string is balanced or not
def isValid(string:str):
    if string[0] != '(' or string[-1] != ')':
        return False
    stack = []
    for i in string:
        # if opening parenthesis is found, push it to stack
        if i == '(':
            stack.append(i)
        elif i == ')':
            # if closing parenthesis is found, pop stack if corresponding opening parenthesis is in stack
            try:
                stack.pop()
            # if closing parenthesis is found but stack is empty, the string is unbalanced
            except IndexError:
                return False
    return len(stack) == 0

# TODO: Find total number of balanced strings
def findWays(n):
    # Check if n is odd, since it is not possible to create any valid parentheses
    if(n & 1):
        return 0
    # Otherwise return n/2'th Catalan Numer
    return catalan(int(n / 2))

class Solution:
    def recurse(self, m:int, n:int, total:int, string = ""):
        if len(parenthesis) >= total:
            return
        if m == 0 and n == 0:
            if isValid(string):
                parenthesis.append(string)
            return
        if m>0:
            self.recurse(m-1,n,total,string+"(")
        if n>0:
            self.recurse(m,n-1,total,string+")")

    def generateParenthesis(self, n: int):
        parenthesis.clear()
        self.recurse(n,n,findWays(2*n))
        return parenthesis

s = Solution()
arr = s.generateParenthesis(1)

for i in arr:
    print(i)