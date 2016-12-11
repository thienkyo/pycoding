# Keep data in { 'key' : 'value' } pair.
# No order in key set.


# Make a dict, add something
age = {}
age['cat'] = 2
age['me'] = 30
age['dog'] = 3
age  # {'cat': 2, 'dog': 3, 'me': 30}

print(age['cat'])  # 2

# Get key list, item list
age.keys()  # ['me', 'dog', 'cat']
age.items()  # [30, 3, 2]

# Delete a key
del age['dog']

# Loop through key:val pair
for key, value in age.items():
    print('{0} : {1}'.format(key, value))

# Get invalid key with default value
age.get('dog', 'No key named \'dog\'.')

# Multivalues dictionary
# Each key holds a list of values
# We can use set instead of list
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)
# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

# Sort dictionary
from operator import itemgetter
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)
# [{'lname': 'Beazley', 'fname': 'David', 'uid': 1002},
# {'lname': 'Cleese', 'fname': 'John', 'uid': 1001},
# {'lname': 'Jones', 'fname': 'Big', 'uid': 1004},
# {'lname': 'Jones', 'fname': 'Brian', 'uid': 1003}]



