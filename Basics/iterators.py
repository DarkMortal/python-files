arr = [1,4,2,5,3,-2,-1,6]

my_iterator = iter(arr)

# next(it1) and it1.__next__() does the same thing

print(next(my_iterator),end = " ")      # prints 1 
print(my_iterator.__next__(),end = " ") # prints 4

# prints the rest of the numbers
for i in my_iterator:
    print(i,end = " ")
print()

# Creating a custom iterator for a list
class myIterator:
    def __init__(self, iterable, someFunction = lambda x:x):
        self.iterable = iterable
        self.index = 0
        self.function = someFunction

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        value = self.iterable[self.index]
        self.index += 1
        return self.function(value)

# Using custom iterator
my_iterator2 = myIterator(arr)
my_iterator3 = myIterator(arr,lambda x:2*x+1)

for item in my_iterator2:
    print(item, end = " ")
print()

for item in my_iterator3:
    print(item, end = " ")
print()

'''
Iterators used when we need more control in the iteration process.
Iterators can enable lazy evaluation, which means that the elements
are generated or fetched only when needed, rather than loading the 
entire sequence into memory upfront. This is particularly useful when
dealing with large or infinite sequences. Loops, on the other hand, typically
require the entire sequence to be available in memory or predefined before execution.
'''