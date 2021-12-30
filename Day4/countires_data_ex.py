from countries_data import countries_data
from pprint import pprint

populatons = []
for c in countries_data:
    populatons.append(c['population'])

sorted_countries = sorted(populatons, reverse=True)
top_ten_coutries = sorted_countries[:10]
top_10 = sorted(countries_data, key=lambda c:c['population'], reverse=True)[:10]
pprint([{'name':c['name'], 'population':c['population']}] for c in top_10)

new_list = []
for c in top_10:
    new_list.append