def permutations(arr):
    result=[]
    if len(arr)==1:
        return [arr[:]]
    for i in range(len(arr)):
        n=arr.pop(0)
        arr2=permutations(arr)
        for j in arr2:
            j.append(n)
        result.extend(arr2)
        arr.append(n)
    return result

if __name__=="__main__":
    nums=permutations([1,2,3])
    print("There are",len(nums),"permutations :\n",nums)