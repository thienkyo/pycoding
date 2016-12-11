# Apply function on each element of a list quickly
# SELECT expression FROM table WHERE conditions
# Common format [ DO_SOMETHING for ITEM in LIST if CONDITION ]

# Time each value with 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
[value * 10 for value in numbers]

# Time each value with 10 if it's greater than 7
[value * 10 for value in numbers if value > 7]

# Return a dictionary
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dict([(number, number * 10) for number in numbers])

# Working with 2 or 3 lists
x = ['x1', 'x2', 'x3']
y = ['y1', 'y2', 'y3']
z = ['z1', 'z2', 'z3']
new_list = [list(tuple_xyz) for tuple_xyz in zip(x, y, z)]
print(new_list)
# [['x1', 'y1', 'z1'], ['x2', 'y2', 'z2'], ['x3', 'y3', 'z3']]

# Unzip
l1, l2, l3 = zip(*new_list)
print(l1)  # ('x1', 'x2', 'x3')
print(l2)  # ('y1', 'y2', 'y3')
print(l3)  # ('z1', 'z2', 'z3')


