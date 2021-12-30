first_name = input('What is your first name? ').title()
last_name = input('What is your last name? ').title()
year_born = int(input('When were you born? '))
current_year = 2021
age = current_year - year_born
city = input('Name of the city your are living in? ').title()
country = input('Conuntry you are living in? ').title()
gender = input('What is your gender F or M? ' ).lower()
pronoun = ''

if gender == 'f' or 'Female':
    pronoun = 'She'
elif gender == 'm' or 'male':
    pronoun = 'He' 


print(f'{pronoun} is {first_name} {last_name}. {pronoun} is {age}. {pronoun} lives in {city} {country} ')