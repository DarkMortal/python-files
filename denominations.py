#This program can compute if a certain value be acheived by a list of denominations

def coin(arr,value):
    if not arr:
        return []
    count=int(value/arr[0])
    rem=int(value%arr[0])
    if count==0:
        return coin(arr[1:len(arr)],value)
    if rem==0:
        return [arr[0]]*count
    else:
        for i in arr[1:len(arr)]:
            if rem%i==0:
                return [arr[0]]*count+[i]*(int(rem/i))
        return coin(arr[1:len(arr)],value)

if __name__=="__main__":
    denominations=[]
    value=int(input("Enter the value = "))
    x=int(input("Enter the denominations and enter -1 when done :\n"))
    while x!=-1:
        denominations.append(x)
        x=int(input())
    denominations=list(filter(lambda x:x<=value,denominations))
    denominations.sort(reverse=True)
    coins=coin(denominations,value)
    if coins:
        print("Value is possible by",coins)
    else:
        print("Value not possible")