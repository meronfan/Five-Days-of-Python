#Data types
#Numbers(int, float, complex)
#Strings - characters
#Booleans (True or False)
#List, Set, Tuple, Dictionary

#Bultin Function we use to check a type: type()

#Numbers(Int, Float, Complex)
print(type(10)) #int
print(type('10')) #str
print(type(9.81)) #float
print(type(1 + 2j)) #complex number

#Strings
#String can be a single character or multiple pages

letter = 'a'
print(letter)
print(len(letter))

word =  'I love Python.'
print(word)
print(len(word))
print(word[0]) #Display l which is the first letter
print(word[1]) #Display o which is the second letter
last_index = len(word) - 1
print(word[last_index])
print(word[2:6]) #slice out love start from 2 index to 5 index

sentence = 'I love Python'
print(sentence.upper())
print(sentence.lower())
print(sentence.count())

#Function can stand by itslef
#Methods should be attached to an object

dna = '''ttggaaccttggaaccttggaaccttggaggaaccttggaaccttggaaccttggaaccttggaacct
     tggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaac
     cttggaaccttggaagaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaacc
     ttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaacctt
     ggaaccttggaaccttggaaccttggaaaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttg
     gaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaaccttggaacc
'''
total_count = len(dna)
a = dna.count('a')
c = dna.count('c')
t = dna.count('t')
g = dna.count('g')
print(a,c,t,g)
print('Proportin',round(a / total_count * 100 , c/total_count,))

#String Methods
#.upper(), .lower(), .count()

sentence = 'I love Python and I love JavaSctipt.'
print(sentence.count('I'))
print(sentence('love'))
print(sentence('I love'))

#case types
print(sentence.title())
print(sentence.swapcase())
print(sentence.startswith('I')) #startwith is boolean returns true
print(sentence.endswith('e')) #endswtith is boolean returns false
print(sentence.index('I')) # returns 0 since the first occurance is on endex 0
print(sentence.find('o')) #find works same way as index if value is not found it ruternse -1
print(sentence.rfind('o')) #finds the word starting from the end of the ist

sentences = 'I love Python I love JavaSctipt. I am looking for a job, I cannot wait to get started.'
print(sentences.split('.'))
print(sentences.split(' '))
words = sentences.split(' ')
print(words)
print(len(words))
print(sentences.count('love') / len(words)) #2 /20

#String Formatting
country = 'Ethiopia'
city = 'Addis Ababa'
gravity = 9.81
mass = 74 #mass in kg
weigth = mass * gravity
#old way of formatting strings
print('%s is in Africa. The captial is %s. '%(country, city))
print('%.2f is the gravitational constant.') %(gravity)
print('The gravity is %.2f and mass is %d in kg and weight is %.2f in Newton.') %(gravity, mass, weigth)

#new way of formating
print('The Better Way')
print('{} is in Africa. The capital is {}.'.format(country, city))
print('{} is the gravitational constant.') %(gravity)
print('The gravity is {} and mass is {} in kg and weight is %.2f in Newton.') %(gravity, mass, weigth)

#the best way of formating
print(f'{country} is in Africa. The capital is {city}.')
print(f'{gravity} is the gravitational constant.')
print(f'The gravity is {gravity} and mass is {mass} in kg and weight is %.2f in Newton.')

a = 4
b = 3
print(f'The sum of {a} and {b} is {a + b }.')
print(f'The difference of {a} and {b} is {a - b}.')
print(f'The product of {a} and {b} is {a * b }.')




