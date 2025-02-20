print('a is {}'.format('1, 2, 3'))
print('My name is {0} {1}. Watashi ha {1} {0}'.format('Jun', 'Sakai'))
print('My name is {name} {family}. Watashi ha {family} {name}'.format(name = 'Jun', family=  'Sakai'))

# f-strings
a = 'a'
print(f'a is {a}')
x, y, z = 1, 2, 3
print(f'a is {x}, {y}. {z}')
print(f'a is {x}. {y}. {z}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')