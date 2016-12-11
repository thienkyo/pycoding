# If
grade = 9
if grade >= 9:
    print('Awesome')
elif grade >= 7:
    print('Good')
elif grade >= 5:
    print('Not bad')
else:
    print('No way')

# Logical operator
if 10 > 5 or 10 < 2:
    print('true')

if 10 > 5 and 10 > 2:
    print('true')

if not 10 < 2:
    print('true')

# For loop
for num in [1, 2, 3]:
    print(num)

for num in range(1, 3):
    print(num)

cats = ['Tom', 'Jerry', 'Cat']
for idx, val in enumerate(cats):
    print(idx, val)

# While
i = 0
while i < 10:
    print('Iteration:', i)
    i = i + 1

# Intervention
for item in [1, 2, 3, 4]:
    if item == 3:
        break  # Stop Loop if see 3
    print(item)

for item in [1, 2, 3, 4]:
    if item == 3:  # Do nothing if see 3, continue the loop
        continue
    print(item)


for i in range(1, 10):
    pass  # Do nothing statement.

