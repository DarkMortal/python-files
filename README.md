# Python practice Files

- In Python3, when arrays are passed to a function, much like javascript, if any changes are done to the array, the original (or any reference to the array) gets changes as well. Example:-
    
      def func(arr):
          arr[0]=22
          arr[len(arr)-1]=33

      if __name__=="__main__":
          a=[1,2,3,4]
          b=a
          print(b)
          func(a)
          print(a)
          print(b)
      #Output
      #[1, 2, 3, 4]
      #[22, 2, 3, 33]
      #[22, 2, 3, 33]
- Lambda functions are written lke this:-

      f=lambda x:3*x*x-2
      print(f(2))   #Will print 10
- Slicing an array from a to b (b not included):- 

      a=arr[a:b], 
      # if arr[:b], then a defaults to arr[1:b]
      # if arr[a:], then a defaults to arr[1:len(arr)]
      # a[:] returns the whole array