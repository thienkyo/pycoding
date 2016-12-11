# Very basic function syntax
def add2(a, b):
    """
    Adding 2 integers.
    """
    return a + b

add2(1, 2)


# Default value
def to_power(a, n = 2):
    """
    Document here.
    """
    return a ** n

to_power(5)


# Return bunch of stuff
def return_many(a, b, c):
    return a * 2, b * 2, c * 2

x, y, z = return_many(2, 3, 4)

# Inline Function
square = lambda x: x * x
square(2)


# Accept any arguments
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

avg(1, 2, 3)


# Accept any keyword argument
def get_html(tag_name, value, **attr):
    print(tag_name)
    print(value)
    attr_grp = ['{0}="{1}"'.format(k, v) for k, v in attr.items()]
    print(attr_grp)

get_html('span', 'value', color='red', size='10')


# Must use keyword arguments
def get_salary(dept, *, user_id):
    print(dept, user_id)

get_salary('IT', 10) # Err
get_salary('IT', user_id=10)

