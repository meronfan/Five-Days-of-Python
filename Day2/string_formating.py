from typing import Counter


first_name = 'Meron'
last_name = 'Fantaye'
country = 'USA'
city = 'Ashburn'
skills = ['Linux','SQL','Python']
age = 300
tech_lang = 'Python'
first_skills = ', '.join(skills[0:-1])
last_skill = skills[-1]

print(f'I am {first_name} {last_name}. I live in {city}, {country}.\nI am learning {tech_lang}. My skills are {first_skills} and {last_skill}. \nI am {age} years old.') 

#join() make a list comma or space separated
print(', '.join([first_skills]))

#strip() remove extra space
print('  i love Python  ')

#replace() find a word and replace
print('I like Python', )