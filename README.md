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

## Outputs
- <b>anonymousFunctions.py</b>

      6
      [6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57]
- <b>classesObjects.py</b>

      It's over 9000!!!
- <b>denominations.py</b>

      Enter the value = 13
      Enter the denominations and enter -1 when done :
      1
      2
      3
      4
      5
      -1
      Value is possible by [5, 5, 3]
- <b>fileHandling.py</b>

      What's the matter clown?
 
      Are you angry, humiliated, is that it?

      Fool, you don't know what humiliation is.
- <b>instanceChecking.py</b>

      True
      True
      False
      True
- <b>maxAverage.py</b>

      ['Ashwin', 'Kohli']
- <b>MRO.py</b>

      Constructor of class A is called
      Value passed from classA = Hello
- <b>permutations.py</b>

      There are 6 permutations :
       [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
- <b>pythogereanTriplets.py</b>

      First 20 triplets between 1 and 100
      (3, 4, 5)
      (4, 3, 5)
      (5, 12, 13)
      (6, 8, 10)
      (7, 24, 25)
      (8, 6, 10)
      (8, 15, 17)
      (9, 12, 15)
      (9, 40, 41)
      (10, 24, 26)
      (11, 60, 61)
      (12, 5, 13)
      (12, 9, 15)
      (12, 16, 20)
      (12, 35, 37)
      (13, 84, 85)
      (14, 48, 50)
      (15, 8, 17)
      (15, 20, 25)
      (15, 36, 39)
- <b>recursions.py</b>

      64
      120
- <b>tuplesDictionary.py</b>

      Enter the name of the person whose details you want to know : 
      Naruto
      Please Enter Full Name
      Naruto Uzumaki

      Phone number : 6290436310
      Village : Konoha
      Rank : Genin

      Sasuke Uchiha

      Phone number : 9836099827
      Village : Konoha
      Rank : Genin

      Kakashi Hatake

      Phone number : 7439302254
      Village : Konoha
      Rank : Jonin

      Nagato Uzumaki

      Member not Found
      Would you like to add it? (Y/N) : y
      Enter the Phone Number : 1234567890
      Enter Rank : Genin
      Enter Village : Hidden Rain
      Nagato Uzumaki

      Phone number : 1234567890
      Village : Hidden Rain
      Rank : Genin
 
