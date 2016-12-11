# String is a List of many character

dummy = 'hello world there'
print(len(dummy))  # 17
print(dummy[4])  # o
print('ello' in dummy)  # True

print(dummy.split(' '))  # ['hello', 'world', 'there']
print('-'.join(['wa', 'iz', 'it']))  # wa-iz-it
print(' strip spaces around me.  '.strip())  # 'strip spaces around me.'


print('Format string: {0:d}, {1:4.2f}, {2}'.format(9, 99.95,
                                                   'This is not real'))
# Format string: 9, 99.95, This is not real

