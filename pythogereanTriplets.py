if __name__=="__main__":
    n=100
    x=20
    #List comprehension
    triplets=[(x,y,z) 
            for x in range(1,n)
            for y in range(1,n)
            for z in range(1,n)
            if x*x+y*y == z*z]
    print("First",x,"triplets between 1 and",n)
    for i in triplets[0:x]:
        print(i)