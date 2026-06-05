# Day 3 of python programming

import math

age = int(27)
height = float(1.63)
complex_number = complex(1 + 2j)


b = int(input('Enter base: '))
h = int(input('Enter height: '))
area = 0.5 * b * h
print(f'The area of the triangle is {area}')

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter = a + b + c

print(f'The perimeter of the triangle is {perimeter}')

rec_length = int(input('Enter length of rectangle: '))
rec_width = int(input('Enter width of rectangle: '))
rec_area = rec_length * rec_width
rec_perimeter = 2 * (rec_length + rec_width)
print(rec_area)
print(rec_perimeter)

radius = int(input('Enter radius: '))
ci_area = math.pi * radius**2
ci_circum = 2 * math.pi * radius
print(ci_area)
print(ci_circum)

print("Slope = 2")
print("x-intercept = 1")
print("y-intercept = -2")

x = -3
y = x**2 + 6*x + 9

len_1 = len('dragon')
len_2 = len('python')

print(len_1 is not len_2)
print('on' in 'python' and 'on' in 'dragon')

sentence = 'I hope this course is not full of jargon.'
print('jargon' in sentence)

print('on' not in 'python' and 'on' in 'dragon')

print(str(float(len_2)))

print(7//3 == int(2.7))

print(int(9.8) == 10)

hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
print(f'Your weekly earning is {hours * rate}.')

years = int(input('Enter number of years you have lived: '))
print(f'You have lived for {years * 365 * 24 * 60 * 60} seconds')

for i in range (1, 6):
    print(i, 1, i, i**2, i**3)