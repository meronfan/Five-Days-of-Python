
def square(n):
    square = n ** 2
    return square

print(square(2))
print(square(6))
print(square(100))

#Calculate weight 

def calculate_weight(mass,gravity):
    weight = mass * gravity
    return f'{weight} N'

print(calculate_weight(75, 9.81))