# Understand Closure first


# Decorator function takes a function as argument
# It adds something to function's behavior
# Like printing something
# Use when we don't want modify function declaration or we can't
# Or you have to time every function
def decorate_what(fn):
    def wrapper(*arg, **kwarg):  # wrapper is a Closure
        print('Before I am in.')
        r = fn(*arg, **kwarg)  # Use state
        print('After I left.')
        return r
    return wrapper


@decorate_what
def do_awesome_thing(number, msg):
    print('Awesome numbers:', number)
    print('Awesome message:', msg)
    return 'Is that cool?'

ret = do_awesome_thing(7, msg='My fav number')
print('Return value:', ret)

# Before I am in.
# Awesome numbers: 7
# Awesome message: My fav number
# After I left.
# Return value: Is that cool?


# Pass argument to Decorator
def pass_a_closure(count, end_msg):
    def decorate_what(fn):
        def wrapper(*arg, **kwarg):
            for i in range(0, count):
                print('Mama, look at me!')
            r = fn(*arg, **kwarg)
            print(end_msg)
            return r
        return wrapper
    return decorate_what


@pass_a_closure(count=3, end_msg='It\' not funny.')
def do_awesome_thing(number, msg):
    print('Awesome numbers:', number)
    print('Awesome message:', msg)
    return 'Is that cool?'

ret = do_awesome_thing(7, msg='My fav number')
print(ret)
# Mama, look at me!
# Mama, look at me!
# Mama, look at me!
# Awesome numbers: 7
# Awesome message: My fav number
# It' not funny.
# Is that cool?

