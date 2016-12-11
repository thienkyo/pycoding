# Function in py is like a variable
# This means: we can pass a function as Argument
# Function can be nested inside a function like a variable
# We can do pretty much stuff with this cool feature


# Closure: A function with state
# Closure can use its parent states
def get_something(var1, var2):  # 2 states of Closure
    def actually_get_something(greeting):  # Closure definition
        msg = greeting + var1 + var2
        return msg
    return actually_get_something  # Use Closure

sth = get_something(var1='Tom', var2='Cat')
print(sth(greeting='Welcome'))  # WelcomeTomCat


# A simple Closure to summary this concept
def print_msg(msg):
    def printer():
        print(msg)
    printer()

print_msg(msg='whadaya mean?')


# Closure attribute
def sample():
    n = 0  # Define global variable for all child of sample function

    def print_n():  # Closure
        print('n =', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n  # Access global variable
        n = value

    # Glue getter/setter to Closure
    print_n.get_n = get_n
    print_n.set_n = set_n
    return print_n

s = sample()
s.set_n(10)
print(s.get_n())  # 10

