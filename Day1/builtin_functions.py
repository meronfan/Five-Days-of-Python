#What is function - a set of code that can perform a specific task and can be reused as needed. 
#2 Types of functions - Built (predefined) and Custom (Defined by the user)
#exit(), print(), len(), input(), round(), sum(), help, dir, int, str, float

#print can take any number of arguments
print('input 1, input 2 whaterve you have any data type')  

#len() returns length of data
skills = ['HTMl', 'CS', 'Python']
print(len(skills))
statment = 'I love Python'
print(len(statment))

#input() recives data from user
#Any data recived using input() is considered as string
first_name = input('Enter your name: ')
year_born = int(input('Enter your birth year: '))
current_year = 2021
print('You are ', first_name)
age = current_year - year_born
print('You are ' + str(age) + 'years old.')

#float() convert input value to float data type
num1 = float(input('Enter a number :'))
print(type(num1))
print(num1)

print(max(100, 1, 2, 50, 80))
print(min(100, 1, 2, 50, 80))

#sum only accepts list data type
print(sum([100, 1, 2, 50, 80]))

#help() give as definition of a funciton 
print(help(str))
keywords = help('keywords')
print(keywords)

#dir returns all the methods associated with spacific data type
first_name = 'John'
print(dir(type(first_name)))


a = 10
print(type(a)) #Print data type of a
print(float(a)) # Convert data type of a to float
print(str(a)) #Convert data type of a to string
print(type(str(10))) # Convert 10 in to string type and display the data type

gravity = 9.81
print(type(gravity)) # Display data type of gravity 
print(int(gravity)) # when we conver float to int there might be loss of data
#The retuned value will be only 9 instade of 9.81

g = '9.81' 
print(float(g))
print(int(float(g)))

#range returns a range of values 
#range(start, end, step)
#by defult start =  0, end = end value - 1, and step = 1
nums = list(range(5))
print(nums) #0, 1, 2, 3, 4

#Print even numbers from 0 to 101
evens = list(range(0 , 101 ,2))
print(evens)

#Print odd numbers from 1 to 101
odds = list(range(1, 101, 2))
print(odds)