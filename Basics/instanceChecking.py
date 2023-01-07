#Checking if an object is an instance of a certain class

class Person:
    pass

class Friend(Person):
    pass

class Parent(Person):
    pass

class Child(Parent):
    pass

alice = Child()

# Is alice an instance of Child? Yes!
print(isinstance(alice, Child))
# True

# Is alice an instance of Parent? Yes!
print(isinstance(alice, Parent))
# True

# Is alice an instance of Friend? No!
print(isinstance(alice, Friend))
# False

# Is alice an instance of Person? Yes!
print(isinstance(alice, Person))
# True

#In Python, the pass keyword is an entire statement in itself.
# This statement doesn't do anything: it's discarded during the byte-compile phase.
# But for a statement that does nothing, the Python pass statement is surprisingly useful.
# Sometimes pass is useful in the final code that runs in production.