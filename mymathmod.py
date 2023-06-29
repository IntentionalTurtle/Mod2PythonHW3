def houseFoot():
    length = input('What is the length of the room in your house in feet?')
    width = input('What is the width of your house in feet?')
    area = float(length) * float(width)
    print(f'Your room is {str(area)} square feet in area!')

def houseFootFast(length,width):
    area = float(length) * float(width)
    print(f'Your room is {str(area)} square feet in area!')

def circumference():
    radius = input("What is the radius of your circle in cm? ")
    circum = 3.1415 * float(radius) * float(2)
    print(f'Your circle has a circumference of {circum} cm^3')

def fastCircumference(radius):
    circum = 3.1415 * float(radius) * float(2)
    print(f'Your circle has a circumference of {circum} cm^3')

