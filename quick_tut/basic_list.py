# Output has same order as input.
# Mutable, which means we can change its item.
# If we want an immutable list, use Tuple.


# Make a list, add something
empty_list = []
empty_list.append(4)
empty_list.append(10)
empty_list.append(True)
empty_list.append(None)
empty_list.append('Hello')
print(empty_list)  # [4, 10, True, None, 'Hello']

# Mutate a list
empty_list[0] = 5
print(empty_list)  # [5, 10, True, None, 'Hello']

# Slice
empty_list[0] # 5
empty_list[:3]  # 5, 10
empty_list[-1]  # 'Hello'
empty_list[3:]  # From True all the way up to the end

# Reverse a list
rank = ['first', 'second', 'third', 'fourth', 'last']
rank[::-1]  # ['last', 'fourth', 'third', 'second', 'first']

# Sort a list
rank = [1, 5, 2, 9, 6]
rank = sorted(rank, reverse=False)
print(rank)  # [1, 2, 5, 6, 9]
