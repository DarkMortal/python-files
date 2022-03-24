def maxAverage(arr):
    d={}
    for i in arr:
        if i[0] in d.keys():
            d[i[0]]=(d[i[0]][0]+i[1],d[i[0]][1]+1)
        else:
            d[i[0]]=(i[1],1)
    e=[]
    for key in d.keys():
        e.append((key,d[key][0]/d[key][1]))
    score=lambda x: x[1]
    return list(sorted(e, key=score))  #In Python, lambda is used to define an anonymous function 

#Driver Code
if __name__=="__main__":
    arr=maxAverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',22),('Ashwin',47)])
    n=len(arr)-1
    max=arr[n][1]
    players=[]
    while max==arr[n][1]:
        players.append(arr[n][0])
        n-=1
    print(players)