# Python practice Files

- In Python3, when arrays are passed to a function, much like javascript, if any changes are done to the array, the original gets changes as well.
- Lambda functions are written lke this:-

      f=lambda x:3*x*x-2
      print(f(2))   #Will print 10
- Slicing an array from a to b (b not included):- 

      a=arr[a:b], 
      # if arr[:b], then a defaults to arr[1:b]
      # if arr[a:], then a defaults to arr[1:len(arr)]
      # a[:] returns the whole array
