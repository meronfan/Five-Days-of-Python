#Create a dictionary called person
#Its values name, age, marital status, skills, hobbies, family, address
#Used list for skills and hobbies, tuple for sisters and parents and dictonary for address

person = {
'first name' : 'Meron', 
'last name': 'Kebede',
'age': 30, 
'is_married': True,
'skills':['SQL', 'Lunix','Python'],
'hobbies':['Reading','Walking'],
'brothers' : ('Abiy','Dawit'),
'sisters':('Hana','Tigist'), 
'parents':('Fantaye', 'Feleketch'),
'spouse':'Tamirat',
'daughter':'Efrata',
'address':{
            'street Name':'20862 Isherwood Ter', 
            'city':'Ashburn',
            'state':'VA',
            'zip code':'20147', 
            'country':'USA' 
             }
}

#print values of the person dictonary 
for key, value in person.items():
    print(key, ' : ', value)
           