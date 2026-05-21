# Day 2: 30 days of python programming

import math

# Level 1
first_name = 'Stella'
last_name = 'McCartney'
full_name = first_name + last_name
country = 'USA'
city = 'Chicago'
age = 37
year = 1989
is_married = False
is_true = False
is_light_on = True

cow, dog, cat, high = 'moo', 'woof', 'miau', 'hell yeah'

# Level 2
print(type(first_name))
print(type(age))
print(type(is_light_on))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one*num_two
division = num_one/num_two
remainder = num_one % num_two
exp = num_one**num_two
flooar_division = num_one // num_two

radius = int(input('Please enter a radius: '))
area_of_circle = math.pi * radius**2
circum_of_circle = 2*math.pi*radius

print(f'Area of circle: {area_of_circle}')
print(f'Circumfrence of circle: {circum_of_circle}')

first_name = input('First name: ')
last_name = input('Last name: ')
country = input('Country: ')
age = input('Age: ')