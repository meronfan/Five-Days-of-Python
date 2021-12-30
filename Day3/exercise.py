"""
#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return f'The sum of {num1} and {num2} is {total}'

num1 = int(input('Enter the first number '))
num2 = int(input('Enter the second number '))
print(add_two_numbers(num1, num2))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle_area(r):
    pi = 3.14
    area = pi * r * r
    return f'Area of a cirlce with radius {r} is {area}.'

radius = int(input('Enter radius of the circle '))
area = circle_area(radius)
print(area)
 """
#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.
