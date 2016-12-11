class Animal(object):
    """
    This is the animal class, an abstract one.
    """

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name)


a = Animal('What is sound of Animal?')
a.talk()  # What is sound of Animal?


class Cat(Animal):
    def talk(self):
        print('I\'m a real one,', self.name)

c = Cat('Meow')
c.talk()  # I'm a real one, Meow


# Compare 2 variables reference to a same object
a = [1, 2, 3]
b = a
print(b is a)  # True

# Check if 2 variables hold same values
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
print(a == b)  # True

# None is an Object
print(None is None)  # True
