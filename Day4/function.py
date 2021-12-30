def calculate_area_rectangle(lenght, width):
    area = lenght * width
    return area

#print(calculate_area_rectangle(10, 20))
#print(calculate_area_rectangle(60, 80))


def calculate_perimeter(lenght, width):
    perimeter = 2 * (lenght + width)
    return perimeter

#print(calculate_perimeter(8, 60))
#print(calculate_perimeter(100, 200))


from countries_list import countries
from pprint import pprint
def get_countries_with_five_letter():
    five_letter = []
    for c in countries:
        if len(c) == 5:
            five_letter.append(c)
    return five_letter

#pprint(get_countries_with_five_letter())

def get_countries_startwith_e():
    startswith_e = []
    for c in countries:
        if c.startswith('E'):
            startswith_e.append(c)
    return startswith_e

pprint(get_countries_startwith_e())
