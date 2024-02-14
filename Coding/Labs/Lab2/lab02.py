# Jacquelyn Xu gqj3wx

# Taks 1: Cylinders
pi = 3.14
a = float(input("Radius: "))
b = float(input("Height: "))
# surface area
def cal_surface_area(r, h):
    surface_area = 2 * pi * r * h + 2 * pi * r ** 2
    return surface_area

s = cal_surface_area(a, b)
print("Surface Area:", s)

# volume
def cal_volume(r, h):
    volume = pi * r ** 2 * h
    return volume

v = cal_volume(a, b)
print("Volume:", v)

# lateral area
def cal_lateral_area(r, h):
    lateral_area = 2 * pi * r * h
    return lateral_area

l = cal_lateral_area(a, b)
print("Lateral Area:", l)

def base_area(r, h):
    base_area = pi * r ** 2
    return base_area

b = base_area(a, b)
print("Base Area:", b)


# Task 2: Mileage
# write a function that allows
# you to input the MPG (miles per gallon) of both vehicles, the length of your trip in miles, and the
# cost per gallon of gas and use it to output the total amount you would save if you chose the
# hybrid over the truck.
def amount_save():
    length = float(input("What is the length of your trip (miles)? "))
    truck = float(input("Enter miles per gallon for your truck (gas): "))
    hybrid = int(input("Enter miles per gallon for your car (hybrid): "))
    cost = float(input("Enter cost of gas (dollars per gallon): "))
    no_gallon_truck = length / truck
    no_gallon_car = length / hybrid
    cost_of_truck = no_gallon_truck * cost
    cost_of_car = no_gallon_car * cost
    difference = cost_of_truck - cost_of_car
    return difference

difference = amount_save()

print("You will save $" + str(difference) + " by renting the hybrid car")




