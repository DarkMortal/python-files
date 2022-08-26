'PS : Given a string s, return the longest palindromic substring in s'

def isPalindrome(s: str) -> bool:
    '''n = len(s)
    x = n>>1
    for i in range(x):
        if s[i] != s[n-i-1]:
            return False
    return True'''
    rev = s[::-1]
    return (s == rev)

dataArr = []

class Solution:
    def createDataTable(self,word: str):
        for i in range(len(word)):
            if i == len(word)-1:
                dataArr.append([1])
            else:
                arr = []
                for j in range(i,i+2):
                    arr.append(1 if isPalindrome(word[i:j+1]) else 0)
                dataArr.append(arr[:])
        for i in range(2,len(word)):
            for j in range(i-1):
                f = (0 if j == i-2 else -1)
                dataArr[j] += [1 if (word[i] == word[j] and dataArr[j+1][f] == 1) else 0]

    def longestPalindrome(self, word: str) -> str:
        dataArr.clear()
        if isPalindrome(word):
            return word
        self.createDataTable(word)
        oldStr = ""
        num = len(dataArr)
        for i in range(num-1):
            newStr = word[i:len(dataArr[i]) - dataArr[i][::-1].index(1)+i]
            if len(newStr) >= len(oldStr):
                oldStr = newStr
        return oldStr

s = Solution()

print(s.longestPalindrome("babad"))
print(s.longestPalindrome("AAABAA"))